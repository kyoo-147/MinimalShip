#!/usr/bin/env python3
"""Check MinimalShip workflow, state, routing and behavioral-eval contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needles: tuple[str, ...], label: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise SystemExit(f"FAIL: {label} is missing: {', '.join(missing)}")


def main() -> int:
    root = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    features = (ROOT / "templates" / "FEATURES.md").read_text(encoding="utf-8")
    run = (ROOT / "templates" / "RUN.md").read_text(encoding="utf-8")
    routing = (ROOT / "references" / "stack-routing.md").read_text(encoding="utf-8")
    try:
        scenarios = json.loads((ROOT / "evals" / "scenarios.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"FAIL: could not read behavioral scenarios: {exc}") from exc

    phases = ("READ", "CLARIFY", "FEATURES", "SPEC", "PLAN", "APPROVE", "DISPATCH", "BUILD", "VERIFY", "SHIP", "ITERATE")
    positions = [root.index(f"## {index}. {phase}") for index, phase in enumerate(phases, start=1)]
    if positions != sorted(positions):
        raise SystemExit("FAIL: workflow phases are not ordered READ through ITERATE")

    require(
        root,
        (
            "Do not start code-changing work or spawn workers merely because",
            "explicitly authorized implementation",
            "FEATURES.md",
            "RUN.md",
            "PASS",
            "FAIL",
            "BLOCKED",
            "neutral defaults",
            "one bounded result",
            "No two active code-changing workers own the same mutable file",
            "A feature is `DONE` only after every required acceptance criterion has evidence",
            "Never mark a feature `DONE` from a plan",
            "references/stack-routing.md",
            "evals/scenarios.json",
        ),
        "root workflow contract",
    )
    require(
        features,
        (
            "EXISTING VERIFIED",
            "REQUESTED",
            "MUST",
            "NICE",
            "NOT NOW",
            "TODO",
            "READY",
            "IN_PROGRESS",
            "VERIFYING",
            "DONE",
            "BLOCKED",
            "Acceptance criteria",
            "Owner",
        ),
        "feature inventory template",
    )
    require(
        run,
        (
            "Primary objective",
            "Branch / worktree",
            "Current MUST scope",
            "Confirmed decisions",
            "Approved execution policy",
            "Tasks and ownership",
            "Definition of done / check",
            "Active workers and dependencies",
            "Verification and evidence",
            "Resume checkpoint",
            "Current blockers",
            "Exact next action",
            "Last meaningful update",
        ),
        "run checkpoint template",
    )
    require(
        routing,
        (
            "Cloudflare",
            "Expo/EAS",
            "Vercel Agent Skills",
            "auto-install",
            "Existing configuration",
            "loading, empty, error",
            "device/emulator",
            "rendered behavior",
            "accessibility",
            "performance",
            "BLOCKED",
        ),
        "stack-routing reference",
    )
    expected_ids = [f"E{index:02d}" for index in range(1, 9)]
    if scenarios.get("scenario_ids") != expected_ids or [item.get("id") for item in scenarios.get("scenarios", [])] != expected_ids:
        raise SystemExit("FAIL: behavioral evals are not exactly E01-E08")
    print("PASS: READ-to-ITERATE workflow, state, routing and E01-E08 contracts are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
