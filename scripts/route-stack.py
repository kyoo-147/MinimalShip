#!/usr/bin/env python3
"""Recommend opt-in official skill families from bounded manifest/import evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

EXCLUDED_DIRS = {".git", ".pi", ".herdr", ".venv", "venv", "node_modules", "dist", "build", ".next", "coverage", "docs", "analysis", ".local", "references", "handbook", "evals"}
SOURCE_SUFFIXES = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
CONFIG_NAMES = {"package.json", "wrangler.toml", "wrangler.json", "wrangler.jsonc", "eas.json", "app.json", "vercel.json"}
TASK_RE = re.compile(r"\b(?:ui|interface|component\w*|render\w*|accessib\w*|performance|responsive|frontend|screen\w*|navigation|native)\b", re.I)
IMPORT_RE = re.compile(r'''(?:\bfrom\s*|\bimport\s*|\brequire\s*\(\s*|\bimport\s*\(\s*)["'](react(?:/[^"']*)?|react-dom(?:/[^"']*)?|react-native(?:/[^"']*)?|next(?:/[^"']*)?|expo(?:/[^"']*)?|@expo/[^"']+|cloudflare:workers)["']''')


def project_evidence(root: Path) -> tuple[dict[str, list[str]], list[str]]:
    signals: dict[str, list[str]] = {key: [] for key in ("cloudflare", "expo", "web", "native", "vercel-host")}
    errors: list[str] = []
    scanned = 0
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS and not (Path(directory) / name).is_symlink())
        for name in sorted(names):
            path = Path(directory) / name
            if path.is_symlink() or (name not in CONFIG_NAMES and path.suffix not in SOURCE_SUFFIXES):
                continue
            scanned += 1
            if scanned > 2000:
                errors.append("Evidence scan limited to 2000 candidate files; inspect the remaining stack manually.")
                return signals, errors
            relative = path.relative_to(root).as_posix()
            if name.startswith("wrangler."):
                signals["cloudflare"].append(relative)
            elif name == "eas.json":
                signals["expo"].append(relative)
            elif name == "vercel.json":
                signals["vercel-host"].append(relative)
            try:
                with path.open(encoding="utf-8", errors="replace") as handle:
                    text = handle.read(200_001)
                if len(text) > 200_000:
                    errors.append(f"Skipped oversized evidence file: {relative}")
                    continue
                if name in {"package.json", "app.json"}:
                    data = json.loads(text)
                    if not isinstance(data, dict):
                        raise ValueError("expected a JSON object")
                    if name == "app.json":
                        if isinstance(data.get("expo"), dict):
                            signals["expo"].append(relative)
                        continue
                    dependencies: set[str] = set()
                    for field in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
                        value = data.get(field, {})
                        if isinstance(value, dict):
                            dependencies.update(value)
                    if "wrangler" in dependencies or "@cloudflare/workers-types" in dependencies:
                        signals["cloudflare"].append(relative)
                    if "expo" in dependencies or any(dep.startswith("@expo/") for dep in dependencies):
                        signals["expo"].append(relative)
                    if dependencies & {"react", "react-dom", "next"}:
                        signals["web"].append(relative)
                    if "react-native" in dependencies:
                        signals["native"].append(relative)
                elif path.suffix in SOURCE_SUFFIXES:
                    # Match module specifiers, not arbitrary words such as "next item" or "build".
                    for match in IMPORT_RE.finditer(text):
                        module = match.group(1)
                        family = "cloudflare" if module == "cloudflare:workers" else "expo" if module == "expo" or module.startswith(("expo/", "@expo/")) else "native" if module.startswith("react-native") else "web"
                        signals[family].append(relative)
            except (OSError, ValueError) as exc:
                errors.append(f"Could not inspect {relative}: {exc}")
    return {key: sorted(set(value)) for key, value in signals.items()}, errors


def detect(root: Path, task: str = "") -> dict[str, Any]:
    if not root.is_dir():
        raise ValueError(f"Project directory does not exist: {root}")
    signals, errors = project_evidence(root)
    routes: list[dict[str, Any]] = []
    qa: list[str] = []
    if signals["cloudflare"]:
        routes.append({"family": "cloudflare", "official_source": "https://github.com/cloudflare/skills", "skills": ["cloudflare"], "evidence_files": signals["cloudflare"]})
        qa.append("Verify existing config/bindings and relevant local runtime/API failure behavior; unavailable runtime is BLOCKED.")
    if signals["expo"]:
        routes.append({"family": "expo", "official_source": "https://github.com/expo/skills", "skills": ["expo-overview"], "evidence_files": signals["expo"]})
        qa.append("Require loading/empty/error/content, relevant retry/offline/navigation/safe-area checks and device/emulator evidence; unavailable native runtime is BLOCKED.")
    if (signals["web"] or signals["native"]) and TASK_RE.search(task):
        skills = []
        if signals["native"]:
            skills.append("react-native-skills")
        if signals["web"]:
            skills.append("react-best-practices" if re.search(r"\b(?:performance|render\w*)\b", task, re.I) else "web-design-guidelines")
        routes.append({"family": "vercel-agent-skills", "official_source": "https://github.com/vercel-labs/agent-skills", "skills": skills, "evidence_files": sorted(set(signals["web"] + signals["native"]))})
        qa.append("Verify rendered behavior, accessibility and relevant performance; React Native also requires device/emulator evidence.")
    return {
        "project": str(root), "task": task, "routes": routes,
        "evidence_files": sorted({path for paths in signals.values() for path in paths}),
        "inspection": "PARTIAL" if errors else "COMPLETE", "inspection_errors": errors,
        "reasons": ["Only manifest, configuration and module-import signals select routes; hosting alone does not."],
        "qa_gates": qa,
        "permissions": dict.fromkeys(("auto_install", "auto_vendor", "auto_upgrade", "auto_change_stack", "auto_deploy", "paid_cloud_or_eas", "use_credentials"), False),
        "no_auto_action": True,
        "capability_policy": "Missing browser, native, device/emulator or runtime capability is BLOCKED, not PASS.",
    }


def self_test() -> None:
    cases = [
        ("generic", {"src/main.ts": 'const nextItem = "react cloudflare expo";'}, "build a UI", []),
        ("prose", {"package.json": '{"description":"react next expo wrangler"}'}, "audit UI", []),
        ("cloudflare", {"wrangler.toml": "name='x'"}, "debug the worker", ["cloudflare"]),
        ("expo", {"package.json": '{"dependencies":{"expo":"1"}}'}, "fix the API screen", ["expo"]),
        ("eas", {"eas.json": "{}"}, "review QA", ["expo"]),
        ("rn", {"package.json": '{"dependencies":{"react-native":"1"}}'}, "improve native UI", ["vercel-agent-skills"]),
        ("next-ui", {"package.json": '{"dependencies":{"next":"1","react":"1"}}'}, "audit UI accessibility", ["vercel-agent-skills"]),
        ("cloudflare-react", {"wrangler.json": "{}", "package.json": '{"dependencies":{"react":"1"}}'}, "improve the frontend UI", ["cloudflare", "vercel-agent-skills"]),
        ("vercel-host", {"vercel.json": "{}"}, "deploy to Vercel", []),
        ("react-backend", {"package.json": '{"dependencies":{"react":"1"}}'}, "fix the backend queue", []),
        ("build-substring", {"package.json": '{"dependencies":{"react":"1"}}'}, "build the backend", []),
        ("dependencies", {"node_modules/example/package.json": '{"dependencies":{"expo":"1"}}'}, "audit UI", []),
        ("import", {"src/ui.tsx": 'import React from "react";'}, "improve rendering", ["vercel-agent-skills"]),
        ("app", {"app.json": '{"expo":{"name":"x"}}'}, "inspect", ["expo"]),
        ("generic-app", {"app.json": '{"name":"x"}'}, "inspect UI", []),
        ("bad-json", {"package.json": '{invalid'}, "audit UI", []),
    ]
    for name, files, task, expected in cases:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, content in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            result = detect(root, task)
            actual = [route["family"] for route in result["routes"]]
            assert actual == expected, f"{name}: expected {expected}, got {actual}"
            assert all(value is False for value in result["permissions"].values())
            if name == "bad-json":
                assert result["inspection"] == "PARTIAL"
            if name == "rn":
                assert result["routes"][0]["skills"] == ["react-native-skills"]
    print(f"PASS: route-stack self-test ({len(cases)} positive/negative fixtures)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", default=".")
    parser.add_argument("--task", default="")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    try:
        result = detect(Path(args.project).expanduser().resolve(), args.task)
    except ValueError as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if result["inspection"] == "PARTIAL" else 0


if __name__ == "__main__":
    sys.exit(main())
