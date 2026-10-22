#!/usr/bin/env python3
"""Capture no-tools Pi fixture decisions against the actual workflow text."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AUTH_ERROR_RE = re.compile(r"unauthorized|authentication|not authenticated|invalidated|oauth|token|api.key|billing|not supported|unknown model|model.*not found|no.*credentials", re.I)


def load_grader() -> Any:
    spec = importlib.util.spec_from_file_location("minimalship_grader", ROOT / "scripts/grade-evals.py")
    if spec is None or spec.loader is None:
        raise ValueError("Cannot load deterministic grader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_json_object(text: str) -> dict[str, Any]:
    # Accept a single optional Markdown fence, but not prefix prose or trailing objects.
    cleaned = text.strip()
    if cleaned.startswith("```json\n") and cleaned.endswith("\n```"):
        cleaned = cleaned[8:-4]
    try:
        value = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Expected one complete JSON response: {exc}") from exc
    if not isinstance(value, dict) or set(value) != {"evidence", "observed_behavior", "next_action"}:
        raise ValueError("Expected exactly evidence, observed_behavior and next_action")
    if not isinstance(value["evidence"], dict) or not isinstance(value["observed_behavior"], str) or not isinstance(value["next_action"], str):
        raise ValueError("Evidence must be an object; observations and next action must be text")
    return value


def command_for(pi: str, model: str) -> list[str]:
    return [pi, "--no-session", "--print", "--no-tools", "--no-extensions", "--no-skills", "--no-mcp", "--no-context-files", "--no-prompt-templates", "--no-themes", "--offline", "--model", model, "--thinking", "low", "--mode", "text", "--"]


def invoke(pi: str, model: str, scenario: dict[str, Any], timeout: int, workflow: str, shape: dict[str, Any]) -> dict[str, Any]:
    sid = scenario["id"]
    prompt = (
        "Apply the real MinimalShip workflow below to this controlled fixture. Produce planning decisions only; no tools are available. "
        "Return exactly one JSON object with evidence (object), observed_behavior (string), next_action (string). "
        "Do not grade yourself or claim command execution. This tests decisions from fixture facts, not product runtime behavior. "
        "Use the evidence shape below; replace type descriptions with your actual decisions. Family IDs are cloudflare, expo, vercel-agent-skills. "
        "QA gate IDs are local-runtime, rendered-behavior, accessibility, performance. Use exact fixture decision IDs and literal status values.\n"
        f"<workflow>\n{workflow}\n</workflow>\n<scenario>\n{scenario['prompt']}\n</scenario>\n"
        f"<fixture>\n{json.dumps(scenario['fixture_data'])}\n</fixture>\n<evidence-shape>\n{json.dumps(shape)}\n</evidence-shape>"
    )
    command = command_for(pi, model)
    # Prompt files avoid CMD multiline truncation, shell metacharacters and argument limits.
    with tempfile.TemporaryDirectory(prefix="minimalship-eval-") as directory:
        workspace = Path(directory)
        agent_dir = workspace / "agent"
        agent_dir.mkdir(mode=0o700)
        source_agent = Path(os.environ.get("PI_CODING_AGENT_DIR", Path.home() / ".pi/agent")).expanduser()
        auth = source_agent / "auth.json"
        # Only existing model authentication is carried over; no extensions, settings, hooks,
        # private profile, model overrides, project credentials or other skills are copied.
        if auth.is_file():
            fd = os.open(agent_dir / "auth.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as handle:
                handle.write(auth.read_bytes())
        prompt_path = workspace / "prompt.txt"
        prompt_path.write_text(prompt, encoding="utf-8")
        env = {**os.environ, "PI_CODING_AGENT_DIR": str(agent_dir)}
        try:
            completed = subprocess.run(command + [f"@{prompt_path}"], cwd=workspace, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {"id": sid, "status": "BLOCKED", "blocker_kind": "timeout" if isinstance(exc, subprocess.TimeoutExpired) else "runtime", "evidence": {"reason": str(exc)}, "command": command + ["@<temporary-prompt.txt>"]}
    capture = {"id": sid, "command": command + ["@<temporary-prompt.txt>"], "stdout": completed.stdout, "stderr": completed.stderr, "exit_code": completed.returncode, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    if completed.returncode:
        combined = completed.stdout + completed.stderr
        return {**capture, "status": "BLOCKED" if AUTH_ERROR_RE.search(combined) else "FAIL", "blocker_kind": "auth", "evidence": {"reason": combined or f"Pi exited {completed.returncode}"}}
    try:
        parsed = extract_json_object(completed.stdout)
    except (ValueError, TypeError) as exc:
        return {**capture, "status": "FAIL", "evidence": {"reason": str(exc)}}
    return {**capture, **parsed, "status": "CAPTURED"}


def baseline_comparison(report: dict[str, Any], baseline_path: Path | None, grader: Any) -> dict[str, Any]:
    if baseline_path is None:
        return {"status": "NOT_MEASURED", "reason": "No captured baseline report supplied; scenario hypotheses are not measurements."}
    baseline = grader.read_json(baseline_path)
    if not isinstance(baseline, dict):
        raise ValueError("Baseline must be a captured report object")
    fields = ("model", "scenario_sha256", "fixture_sha256")
    if any(baseline.get("provenance", {}).get(field) != report["provenance"][field] for field in fields):
        raise ValueError("Baseline model/scenarios/fixtures differ; comparison is not controlled")
    graded = grader.grade_report(baseline)
    if graded["errors"]:
        raise ValueError("Baseline report is malformed")
    before = {row["id"]: row["status"] for row in graded["results"]}
    return {"status": "MEASURED", "baseline_report_sha256": digest(baseline_path), "baseline_workflow_sha256": baseline["provenance"].get("workflow_sha256"), "results": [{"id": row["id"], "before": before[row["id"]], "after": row["status"]} for row in report["grading"]["results"]]}


def self_test() -> int:
    for invalid in ('{} {}', 'prose {"evidence":{}}', '[1]', '{"status":"PASS","evidence":{}}'):
        try:
            extract_json_object(invalid)
        except ValueError:
            continue
        raise AssertionError(f"accepted invalid capture: {invalid}")
    assert extract_json_object('{"evidence":{},"observed_behavior":"x","next_action":"y"}')["evidence"] == {}
    command = command_for("pi", "explicit-model")
    assert all(flag in command for flag in ("--no-extensions", "--no-tools", "--no-skills", "--offline"))
    print("PASS: runner rejects ambiguous output and disables tools/extensions/discovery")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="JSON is always emitted")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--model", default=os.environ.get("MINIMALSHIP_EVAL_MODEL"), help="explicitly authorized provider/model; no implicit paid fallback")
    parser.add_argument("--workflow", type=Path, default=ROOT / "SKILL.md", help="workflow under test (use a saved baseline SKILL.md for baseline capture)")
    parser.add_argument("--baseline", type=Path, help="captured baseline report using identical fixtures/model")
    parser.add_argument("--output", type=Path, help="retain the full report in a private path such as .local/")
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()
    try:
        grader = load_grader()
        if args.self_test:
            return self_test()
        scenarios = grader.load_scenarios()
        if args.check:
            print(json.dumps({"status": "PASS", "scenarios": list(scenarios)}))
            return 0
        if args.timeout <= 0:
            raise ValueError("timeout must be positive")
        workflow_path = args.workflow.resolve()
        workflow = workflow_path.read_text(encoding="utf-8")
        routing = (ROOT / "references/stack-routing.md").read_text(encoding="utf-8")
        pi = shutil.which("pi")
        results = []
        for sid, scenario in scenarios.items():
            if not pi or not args.model:
                results.append({"id": sid, "status": "BLOCKED", "blocker_kind": "runtime", "evidence": {"reason": "pi executable or explicit --model/MINIMALSHIP_EVAL_MODEL unavailable"}})
            else:
                context = workflow + (f"\n<stack-routing-reference>\n{routing}\n</stack-routing-reference>" if sid in {"E07", "E08"} else "")
                results.append(invoke(pi, args.model, scenario, args.timeout, context, grader.SHAPES[sid]))
        version = subprocess.run([pi, "--no-extensions", "--version"], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, check=False) if pi else None
        report = {
            "schema_version": 2, "mode": "fixture-decisions-no-tools", "scope": "Not a live product, browser, native or worker-dispatch test",
            "provenance": {"model": args.model, "platform": platform.platform(), "pi_version": version.stdout.strip() if version and version.returncode == 0 else "unavailable", "workflow_sha256": digest(workflow_path), "scenario_sha256": digest(ROOT / "evals/scenarios.json"), "routing_sha256": digest(ROOT / "references/stack-routing.md"), "fixture_sha256": {sid: digest(ROOT / "evals/fixtures" / sid / "input.json") for sid in scenarios}},
            "results": results,
        }
        report["grading"] = grader.grade_report(report)
        report["baseline_comparison"] = baseline_comparison(report, args.baseline, grader)
        status = report["grading"]["status"]
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        report = {"status": "FAIL", "errors": [str(exc)]}
        status = "FAIL"
    serialized = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[status]


if __name__ == "__main__":
    sys.exit(main())
