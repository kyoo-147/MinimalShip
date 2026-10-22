#!/usr/bin/env python3
"""Report whether a private MinimalShip profile is ready for use."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

QUESTION_RE = re.compile(r"^(?:## P\d+\.|\d+\.\s)")
REQUIRED_MODULES = (
    "VOICE.md",
    "OPINIONS.md",
    "BUILD_PLAYBOOK.md",
    "TASTE_UI.md",
    "RESEARCH_TASTE.md",
    "UI_TESTING.md",
    "ORCHESTRATION.md",
    "PERMISSIONS.md",
)


def resolve_profile_dir(argument: Path | None) -> Path | None:
    if argument is not None:
        return argument.expanduser().resolve()
    configured = os.environ.get("MINIMALSHIP_PROFILE_DIR", "").strip()
    if configured:
        return Path(configured).expanduser().resolve()
    agent_dir = os.environ.get("PI_CODING_AGENT_DIR", "").strip()
    if agent_dir:
        return Path(agent_dir).expanduser().resolve() / "profile"
    return None


def questions(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if QUESTION_RE.match(line)]


def print_questions(path: Path) -> None:
    print("Answer every question below, or explicitly use `not applicable` or `use neutral defaults`.")
    for line in questions(path):
        print(f"- {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a private MinimalShip profile")
    parser.add_argument(
        "--profile-dir",
        type=Path,
        help="Private profile directory; defaults to MINIMALSHIP_PROFILE_DIR or PI_CODING_AGENT_DIR/profile",
    )
    args = parser.parse_args()

    profile_dir = resolve_profile_dir(args.profile_dir)
    public_questions = Path(__file__).resolve().parents[1] / "templates" / "profile" / "PROFILE-QUESTIONS.md"
    if profile_dir is None:
        print("BLOCKED: PROFILE_INCOMPLETE")
        print("No private profile directory was configured.")
        print_questions(public_questions)
        return 1

    profile_file = profile_dir / "PROFILE.md"
    question_file = profile_dir / "PROFILE-QUESTIONS.md"
    if not profile_file.is_file() or not question_file.is_file():
        print("BLOCKED: PROFILE_INCOMPLETE")
        print(f"Missing profile files under: {profile_dir}")
        print_questions(public_questions)
        return 1
    missing_modules = [name for name in REQUIRED_MODULES if not (profile_dir / name).is_file()]
    if missing_modules:
        print("BLOCKED: PROFILE_INCOMPLETE")
        print(f"Missing profile modules: {', '.join(missing_modules)}")
        print_questions(public_questions)
        return 1

    profile_text = profile_file.read_text(encoding="utf-8")
    status_line = next(
        (line.strip() for line in profile_text.splitlines() if line.strip().startswith("- status:")),
        "- status: incomplete",
    )
    if "status: complete" not in status_line.lower() or "?" in profile_text or "[ ]" in profile_text:
        print("BLOCKED: PROFILE_INCOMPLETE")
        print(f"Profile: {profile_dir}")
        print_questions(public_questions)
        return 1

    print("PASS: PROFILE_COMPLETE")
    print(f"Profile: {profile_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
