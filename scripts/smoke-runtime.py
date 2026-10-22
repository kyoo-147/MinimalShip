#!/usr/bin/env python3
"""Report structural/fixture checks and fresh-install Pi/Herdr capability probes."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def status(name: str, value: str, evidence: dict[str, Any]) -> dict[str, Any]:
    return {"check": name, "status": value, "evidence": evidence}


def command_output(command: list[str], *, cwd: Path = ROOT, timeout: int = 30) -> tuple[int, str, str] | None:
    try:
        completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return completed.returncode, completed.stdout, completed.stderr


def load_module(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / f"{name}.py")
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_resume() -> dict[str, Any]:
    text = (ROOT / "RUN.md").read_text(encoding="utf-8")
    required = ("## Resume checkpoint", "Checkpoint ID:", "Last verified:", "Settled requirements:", "Current blockers:", "Exact next action after resume:")
    missing = [marker for marker in required if marker not in text]
    return status("resume-fields-structural", "FAIL" if missing else "PASS", {"missing": missing, "scope": "Field presence only; E06 separately tests fixture decision fidelity, not session restoration."})


def check_fixture_grader() -> dict[str, Any]:
    grader = load_module("grade-evals")
    with contextlib.redirect_stdout(io.StringIO()) as output:
        code = grader.self_test()
    return status("fixture-grader-regressions", "PASS" if code == 0 else "FAIL", {"output": output.getvalue().strip(), "scope": "E01-E08 typed fixture assertions; not live worker enforcement."})


def module_candidates() -> list[Path]:
    candidates = []
    if os.environ.get("MINIMALSHIP_PI_SKILLS_MODULE"):
        candidates.append(Path(os.environ["MINIMALSHIP_PI_SKILLS_MODULE"]))
    appdata = os.environ.get("APPDATA")
    if appdata:
        candidates.append(Path(appdata) / "npm/node_modules/@earendil-works/pi-coding-agent/dist/core/skills.js")
    npm = shutil.which("npm")
    result = command_output([npm, "root", "-g"]) if npm else None
    if result and result[0] == 0:
        candidates.append(Path(result[1].strip()) / "@earendil-works/pi-coding-agent/dist/core/skills.js")
    return [path for path in dict.fromkeys(candidates) if path.is_file()]


def check_fresh_install() -> dict[str, Any]:
    installer = load_module("install")
    sources = [(installer.SKILL_NAME, ROOT, True)] + [(path.name, path, False) for path in installer.promoted_sources(ROOT)]
    with tempfile.TemporaryDirectory(prefix="minimalship-runtime-install-") as directory:
        agent_dir = Path(directory) / "agent"
        target = agent_dir / "skills"
        installer.install_skills(ROOT, target, sources, force=False)
        installed = target / "minimalship"
        required = ["evals/scenarios.json", "references/stack-routing.md", "scripts/run-evals.py", "scripts/grade-evals.py", "scripts/smoke-runtime.py"] + [f"evals/fixtures/E{index:02d}/input.json" for index in range(1, 9)]
        missing = [path for path in required if not (installed / path).is_file()]
        excluded = [name for name in ("FEATURES.md", "RUN.md", "AGENTS.md", "CLAUDE.md", ".local", "docs", "analysis") if (installed / name).exists()]
        hashes = {name: hashlib.sha256((target / name / "SKILL.md").read_bytes()).hexdigest() for name, _, _ in sources}
        if missing or excluded or any(hashes[name] != hashlib.sha256((source / "SKILL.md").read_bytes()).hexdigest() for name, source, _ in sources):
            return status("fresh-install-loader", "FAIL", {"missing": missing, "excluded_present": excluded})
        node = shutil.which("node")
        modules = module_candidates()
        if not node or not modules:
            return status("fresh-install-loader", "BLOCKED", {"install_skill_count": len(hashes), "content_hashes_match": True, "reason": "Node or installed Pi skills loader unavailable; set MINIMALSHIP_PI_SKILLS_MODULE if installed elsewhere."})
        # Explicit paths avoid unrelated global/project skill discovery.
        script = f"""import {{loadSkills}} from {json.dumps(modules[0].resolve().as_uri())};
const result = loadSkills({{agentDir: process.argv[2], skillPaths: [process.argv[2] + '/skills'], includeDefaults: false, cwd: process.argv[2]}});
console.log(JSON.stringify({{names: result.skills.map(s => s.name), diagnostics: result.diagnostics}}));
"""
        script_path = Path(directory) / "loader.mjs"
        script_path.write_text(script, encoding="utf-8")
        result = command_output([node, str(script_path), str(agent_dir)], cwd=agent_dir)
        if result is None:
            return status("fresh-install-loader", "BLOCKED", {"reason": "Pi loader probe could not execute"})
        code, stdout, stderr = result
        if code:
            return status("fresh-install-loader", "FAIL", {"stderr": stderr})
        try:
            report = json.loads(stdout)
        except ValueError as exc:
            return status("fresh-install-loader", "FAIL", {"reason": str(exc), "stdout": stdout})
        expected = sorted(hashes)
        actual = sorted(report.get("names", []))
        clean = actual == expected and not report.get("diagnostics")
        return status("fresh-install-loader", "PASS" if clean else "FAIL", {"expected_names": expected, "actual_names": actual, "diagnostics": report.get("diagnostics"), "workflow_sha256": hashes["minimalship"], "content_hashes_match": True, "scope": "Fresh disposable copy of this checkout, not a global/profile refresh or live skill invocation."})


def check_pi_binary() -> dict[str, Any]:
    pi = shutil.which("pi")
    result = command_output([pi, "--no-extensions", "--version"]) if pi else None
    if result is None:
        return status("pi-binary", "BLOCKED", {"reason": "Pi version probe unavailable"})
    code, stdout, stderr = result
    return status("pi-binary", "FAIL" if code else "PASS", {"version": stdout.strip(), "stderr": stderr})


def check_herdr() -> dict[str, Any]:
    herdr = shutil.which("herdr")
    result = command_output([herdr, "status", "--json"]) if herdr and os.environ.get("HERDR_ENV") == "1" else None
    if result is None:
        return status("herdr-server", "BLOCKED", {"reason": "Herdr-managed pane/status probe unavailable"})
    code, stdout, stderr = result
    if code:
        return status("herdr-server", "FAIL", {"stderr": stderr})
    try:
        server = json.loads(stdout).get("server", {})
    except (ValueError, AttributeError) as exc:
        return status("herdr-server", "FAIL", {"reason": str(exc)})
    if not server.get("running") or not server.get("compatible"):
        return status("herdr-server", "BLOCKED", {"reason": "Server unavailable or incompatible", "server": server})
    return status("herdr-server", "PASS", {"version": server.get("version"), "compatible": True})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="exit 2 for BLOCKED (default is report-only)")
    args = parser.parse_args()
    checks = []
    for check in (check_resume, check_fixture_grader, check_fresh_install, check_pi_binary, check_herdr):
        try:
            checks.append(check())
        except (OSError, ValueError, AssertionError, SystemExit) as exc:
            checks.append(status(check.__name__, "FAIL", {"reason": str(exc)}))
    checks.append(status("live-worker-dispatch", "BLOCKED", {"reason": "Not executed by this non-dispatching probe; requires separately approved task, ownership, worktree and captured worker evidence."}))
    overall = "FAIL" if any(row["status"] == "FAIL" for row in checks) else "BLOCKED" if any(row["status"] == "BLOCKED" for row in checks) else "PASS"
    print(json.dumps({"status": overall, "checks": checks}, indent=2))
    return 1 if overall == "FAIL" else 2 if overall == "BLOCKED" and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
