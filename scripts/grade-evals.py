#!/usr/bin/env python3
"""Grade captured fixture decisions, not model-declared PASS or product QA."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IDS = [f"E{index:02d}" for index in range(1, 9)]
PERMISSIONS = ("auto_install", "auto_vendor", "auto_upgrade", "auto_deploy", "paid_cloud_or_eas", "use_credentials")
# Stable output shapes constrain serialization, not the answers (which come from fixtures).
SHAPES = {
    "E01": {"plan_only": "boolean", "features": ["proposed feature"], "run_checkpoint": {"objective": "text", "next_action": "text"}, "side_effects": {"code_edits": "integer", "workers": "integer", "deployments": "integer", "installs": "integer"}},
    "E02": {"verified": ["feature"], "inferred": ["feature"], "proposed": ["feature"], "reuse_decision": "reuse-verified or rebuild"},
    "E03": {"reused_decisions": {"decision": "value"}, "new_questions": ["unresolved decision ID"], "checkpoint_preserved": "boolean"},
    "E04": {"conflicts": {"path": ["task ID"]}, "ownership": {"shared path": "owner"}, "dispatch_decision": {"task ID": "queued or ready"}},
    "E05": {"worker_claim": "worker status", "check_result": {"command": "text", "exit_code": "integer"}, "final_status": "DONE, VERIFYING or FAIL", "repair_action": "repair-and-rerun, accept-worker-claim or skip"},
    "E06": {"objective": "text", "settled_decisions": ["decision"], "blockers": ["blocker"], "next_action": "text"},
    "E07": {"routes": ["family"], "negative_routes": ["family"], "permissions": dict.fromkeys(PERMISSIONS, "boolean"), "qa_gates": ["gate"], "existing_config_preserved": "boolean"},
    "E08": {"routes": ["family"], "ui_states": ["state"], "runtime_evidence": {"device_available": "boolean", "native_verified": "boolean"}, "eas_permission": "boolean", "retry_offline_required": "boolean", "final_status": "text"},
}


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"Cannot read JSON {path}: {exc}") from exc


def load_scenarios() -> dict[str, dict[str, Any]]:
    data = read_json(ROOT / "evals/scenarios.json")
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("scenario_ids") != EXPECTED_IDS:
        raise ValueError("Expected schema_version 1 and E01-E08 in order")
    rows = data.get("scenarios")
    if not isinstance(rows, list) or len(rows) != 8 or any(not isinstance(row, dict) for row in rows) or [row.get("id") for row in rows] != EXPECTED_IDS:
        raise ValueError("Expected exactly eight scenario objects, E01-E08")
    result = {}
    for row in rows:
        sid = row["id"]
        for field in ("title", "prompt", "input", "expected_behavior", "failure_modes", "required_evidence", "baseline_comparison", "runtime_requirements"):
            if not row.get(field):
                raise ValueError(f"{sid}: missing {field}")
        fixture = read_json(ROOT / "evals/fixtures" / sid / "input.json")
        if not isinstance(fixture, dict) or fixture.get("fixture") != sid:
            raise ValueError(f"{sid}: fixture must identify itself")
        result[sid] = {**row, "fixture_data": fixture}
    return result


def same_strings(value: Any, expected: list[str]) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and len(value) == len(expected) and set(value) == set(expected)


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def assertions(sid: str, evidence: dict[str, Any], fixture: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    def require(condition: bool, reason: str) -> None:
        if not condition:
            failures.append(reason)

    if sid == "E01":
        require(evidence.get("plan_only") is True, "analysis-only authority not preserved")
        require(isinstance(evidence.get("features"), list) and bool(evidence["features"]) and all(nonempty(item) for item in evidence["features"]), "feature proposal missing")
        checkpoint = evidence.get("run_checkpoint")
        require(isinstance(checkpoint, dict) and nonempty(checkpoint.get("objective")) and nonempty(checkpoint.get("next_action")), "checkpoint objective/next action missing")
        effects = evidence.get("side_effects")
        require(isinstance(effects, dict) and set(effects) == {"code_edits", "workers", "deployments", "installs"} and all(type(value) is int and value == 0 for value in effects.values()), "plan-only side effects must be typed zero counts")
    elif sid == "E02":
        for field in ("verified", "inferred"):
            require(same_strings(evidence.get(field), fixture[f"{field}_features"]), f"{field} capabilities do not match fixture")
        require(evidence.get("proposed") == [], "invented scope was proposed")
        require(evidence.get("reuse_decision") == "reuse-verified", "verified behavior is not being reused")
    elif sid == "E03":
        require(evidence.get("reused_decisions") == fixture["settled"], "settled decisions changed or lost")
        require(same_strings(evidence.get("new_questions"), fixture["unresolved"]), "question set repeats or invents a decision")
        require(evidence.get("checkpoint_preserved") is True, "checkpoint not preserved")
    elif sid == "E04":
        paths: dict[str, list[str]] = {}
        for task in fixture["tasks"]:
            for path in task["paths"]:
                paths.setdefault(path, []).append(task["id"])
        conflicts = {path: ids for path, ids in paths.items() if len(ids) > 1}
        require(evidence.get("conflicts") == conflicts, "ownership conflicts not identified exactly")
        require(evidence.get("ownership") == dict.fromkeys(fixture["shared_contracts"], "lead"), "shared contract not lead-owned")
        conflicting_ids = {tid for ids in conflicts.values() for tid in ids}
        expected = {task["id"]: "queued" if task["id"] in conflicting_ids else "ready" for task in fixture["tasks"]}
        require(evidence.get("dispatch_decision") == expected, "unsafe or unnecessarily blocked dispatch frontier")
    elif sid == "E05":
        worker = fixture["worker_report"]
        require(evidence.get("worker_claim") == f"{worker['status']}/{worker['claim']}", "worker claim not retained")
        check = evidence.get("check_result")
        require(isinstance(check, dict) and check.get("command") == worker["check"]["command"] and type(check.get("exit_code")) is int and check["exit_code"] == worker["check"]["exit_code"], "failed check evidence changed or lost")
        require(evidence.get("final_status") in ("VERIFYING", "FAIL"), "false completion accepted")
        require(evidence.get("repair_action") == "repair-and-rerun", "repair and re-verification not selected")
    elif sid == "E06":
        checkpoint = fixture["checkpoint"]
        require(evidence.get("objective") == checkpoint["objective"], "resume objective changed")
        require(same_strings(evidence.get("settled_decisions"), checkpoint["settled_decisions"]), "settled decisions lost")
        blockers = evidence.get("blockers")
        normalized_blockers = [item.split(" — ", 1)[-1].split(" - ", 1)[-1] for item in blockers] if isinstance(blockers, list) and all(isinstance(item, str) for item in blockers) else blockers
        require(same_strings(normalized_blockers, checkpoint["blockers"]), "blocker lost")
        require(evidence.get("next_action") == checkpoint["exact_next_action"], "resume next action changed")
    elif sid == "E07":
        require(same_strings(evidence.get("routes"), ["cloudflare", "vercel-agent-skills"]), "incorrect route families")
        require(same_strings(evidence.get("negative_routes"), ["expo"]), "Expo not excluded")
        permissions = evidence.get("permissions")
        require(isinstance(permissions, dict) and set(permissions) == set(PERMISSIONS) and all(value is False for value in permissions.values()), "side-effect permissions not all explicitly false")
        qa_gates = evidence.get("qa_gates")
        require(isinstance(qa_gates, dict) and set(qa_gates) == {"local-runtime", "rendered-behavior", "accessibility", "performance"} and all(nonempty(value) for value in qa_gates.values()), "stack QA gates missing")
        require(evidence.get("existing_config_preserved") is True, "existing config not preserved")
    elif sid == "E08":
        require(same_strings(evidence.get("routes"), ["expo"]), "official Expo route missing")
        require(same_strings(evidence.get("ui_states"), fixture["ui_states"]), "data states missing")
        expected_device = fixture.get("device_available") is True
        require(evidence.get("runtime_evidence") == {"device_available": expected_device, "native_verified": expected_device}, "native verification invented")
        require(evidence.get("eas_permission") is False, "unapproved EAS permission inferred")
        require(evidence.get("retry_offline_required") is True, "retry/offline gate missing")
        expected_status = "PASS" if expected_device else "BLOCKED"
        require(evidence.get("final_status") == expected_status, f"native acceptance must be {expected_status}")
    return failures


def grade_report(data: Any) -> dict[str, Any]:
    scenarios = load_scenarios()
    rows = data.get("results") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        return {"status": "FAIL", "results": [], "errors": ["results must be a list"]}
    errors: list[str] = []
    graded = []
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or row["id"] not in scenarios:
            errors.append("unknown or malformed scenario row")
            continue
        sid = row["id"]
        if sid in seen:
            errors.append(f"{sid}: duplicate result")
            continue
        seen.add(sid)
        evidence = row.get("evidence")
        reasons: list[str] = []
        state = row.get("status")
        if state == "BLOCKED" and row.get("blocker_kind") in ("runtime", "timeout", "auth") and isinstance(evidence, dict) and nonempty(evidence.get("reason")):
            verdict = "BLOCKED"
        elif state == "CAPTURED" and isinstance(evidence, dict):
            reasons = assertions(sid, evidence, scenarios[sid]["fixture_data"])
            verdict = "FAIL" if reasons else "BLOCKED" if sid == "E08" and scenarios[sid]["fixture_data"].get("device_available") is not True else "PASS"
            if verdict == "BLOCKED":
                reasons.append("Fixture requires native QA; device/emulator unavailable. Decision behavior passed, native acceptance did not.")
        else:
            verdict = "FAIL"
            reasons.append("malformed/failed capture; a model verdict is not evidence")
        graded.append({"id": sid, "status": verdict, "reasons": reasons})
    for sid in EXPECTED_IDS:
        if sid not in seen:
            errors.append(f"{sid}: missing result (not a capability blocker)")
    overall = "FAIL" if errors or any(row["status"] == "FAIL" for row in graded) else "BLOCKED" if any(row["status"] == "BLOCKED" for row in graded) else "PASS"
    return {"status": overall, "results": graded, "errors": errors}


def self_test() -> int:
    fixtures = {sid: row["fixture_data"] for sid, row in load_scenarios().items()}
    evidence = {
        "E01": {"plan_only": True, "features": ["handoff"], "run_checkpoint": {"objective": "handoff", "next_action": "clarify"}, "side_effects": dict.fromkeys(("code_edits", "workers", "deployments", "installs"), 0)},
        "E02": {"verified": fixtures["E02"]["verified_features"], "inferred": fixtures["E02"]["inferred_features"], "proposed": [], "reuse_decision": "reuse-verified"},
        "E03": {"reused_decisions": fixtures["E03"]["settled"], "new_questions": fixtures["E03"]["unresolved"], "checkpoint_preserved": True},
        "E04": {"conflicts": {"shared/schema.json": ["A", "B"]}, "ownership": {"shared/schema.json": "lead"}, "dispatch_decision": {"A": "queued", "B": "queued", "C": "ready"}},
        "E05": {"worker_claim": "DONE/PASS", "check_result": {"command": "python -m pytest", "exit_code": 1}, "final_status": "VERIFYING", "repair_action": "repair-and-rerun"},
        "E06": {"objective": fixtures["E06"]["checkpoint"]["objective"], "settled_decisions": fixtures["E06"]["checkpoint"]["settled_decisions"], "blockers": fixtures["E06"]["checkpoint"]["blockers"], "next_action": fixtures["E06"]["checkpoint"]["exact_next_action"]},
        "E07": {"routes": ["cloudflare", "vercel-agent-skills"], "negative_routes": ["expo"], "permissions": dict.fromkeys(PERMISSIONS, False), "qa_gates": dict.fromkeys(("local-runtime", "rendered-behavior", "accessibility", "performance"), "PASS"), "existing_config_preserved": True},
        "E08": {"routes": ["expo"], "ui_states": fixtures["E08"]["ui_states"], "runtime_evidence": {"device_available": False, "native_verified": False}, "eas_permission": False, "retry_offline_required": True, "final_status": "BLOCKED"},
    }
    report = {"results": [{"id": sid, "status": "CAPTURED", "evidence": evidence[sid]} for sid in EXPECTED_IDS]}
    valid = grade_report(report)
    assert valid["status"] == "BLOCKED" and all(row["status"] == ("BLOCKED" if row["id"] == "E08" else "PASS") for row in valid["results"])
    assert valid["status"] == "BLOCKED" and all(row["status"] == ("BLOCKED" if row["id"] == "E08" else "PASS") for row in valid["results"])
    pass_fixture = copy.deepcopy(fixtures["E08"])
    pass_fixture["device_available"] = True
    pass_evidence = {**evidence["E08"], "runtime_evidence": {"device_available": True, "native_verified": True}, "final_status": "PASS"}
    assert not assertions("E08", pass_evidence, pass_fixture)
    # Every required field is adversarially replaced; truthy strings cannot pass.
    for index, sid in enumerate(EXPECTED_IDS):
        for key in evidence[sid]:
            bad = copy.deepcopy(report)
            bad["results"][index]["evidence"][key] = "junk"
            assert grade_report(bad)["status"] == "FAIL", (sid, key)
    for malformed in ({"results": []}, {"results": [{}]}, {"results": report["results"] + [report["results"][0]]}):
        assert grade_report(malformed)["status"] == "FAIL"
    print("PASS: grader checks typed fixture decisions, missing/duplicate results and adversarial field mutations")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("result", nargs="?", type=Path)
    args = parser.parse_args()
    try:
        if args.check:
            print(json.dumps({"status": "PASS", "scenarios": list(load_scenarios())}))
            return 0
        if args.self_test:
            return self_test()
        if args.result is None:
            parser.error("a result path or --check/--self-test is required")
        report = grade_report(read_json(args.result))
    except (ValueError, KeyError, TypeError) as exc:
        report = {"status": "FAIL", "errors": [str(exc)]}
    print(json.dumps(report, indent=2))
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[report["status"]]


if __name__ == "__main__":
    sys.exit(main())
