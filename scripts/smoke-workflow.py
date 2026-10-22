#!/usr/bin/env python3
"""Check the MinimalShip planning, state, approval and evidence contracts."""

from __future__ import annotations

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

    phases = (
        "UNDERSTAND",
        "CLARIFY",
        "SPECIFY",
        "PLAN",
        "APPROVE",
        "DISPATCH",
        "BUILD",
        "VERIFY",
        "SHIP",
        "IMPROVE",
    )
    positions = [root.index(f"## {index}. {phase}") for index, phase in enumerate(phases, start=1)]
    if positions != sorted(positions):
        raise SystemExit("FAIL: workflow phases are not ordered Understand through Improve")

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
            "Current blockers",
            "Exact next action",
            "Last meaningful update",
        ),
        "run checkpoint template",
    )
    print("PASS: planning, approval, state tracking, bounded dispatch and evidence contracts are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
