#!/usr/bin/env python3
"""Report private-profile readiness without blocking ordinary neutral-default work."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

QUESTION_RE = re.compile(r"^(?:## P\d+\.|\d+\.\s)")
FIELD_RE = re.compile(r"^-\s+[^:\n]+:\s*(.*)$")
UNRESOLVED_ITEM_RE = re.compile(r"^(?:[-*]|\d+\.)\s*\?$|^(?:[-*])\s+[^:\n]+:\s*$")
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
REQUIRED_SCOPES = {
    "permissions": ("PERMISSIONS.md",),
    "orchestration": ("ORCHESTRATION.md",),
    "dispatch": ("PERMISSIONS.md", "ORCHESTRATION.md"),
}


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


def unresolved_fields(text: str) -> list[str]:
    unresolved: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        match = FIELD_RE.match(stripped)
        if match and (not match.group(1).strip() or match.group(1).strip() == "?"):
            unresolved.append(stripped)
        elif UNRESOLVED_ITEM_RE.match(stripped):
            unresolved.append(stripped)
    return unresolved


def missing_profile_files(profile_dir: Path) -> list[str]:
    required = ("PROFILE.md", "PROFILE-QUESTIONS.md", *REQUIRED_MODULES)
    return [name for name in required if not (profile_dir / name).is_file()]


def unresolved_modules(profile_dir: Path, modules: tuple[str, ...]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for name in modules:
        path = profile_dir / name
        if not path.is_file():
            result[name] = ["missing file"]
            continue
        fields = unresolved_fields(path.read_text(encoding="utf-8"))
        if fields:
            result[name] = fields
    return result


def status_line(profile_text: str) -> str:
    return next(
        (line.strip() for line in profile_text.splitlines() if line.strip().startswith("- status:")),
        "- status: incomplete",
    )


def blocked(scope: str, profile_dir: Path | None, public_questions: Path) -> int:
    label = {
        "profile": "PROFILE_INCOMPLETE",
        "permissions": "PERMISSIONS_UNRESOLVED",
        "orchestration": "ORCHESTRATION_UNRESOLVED",
        "dispatch": "DISPATCH_POLICY_UNRESOLVED",
    }[scope]
    print(f"BLOCKED: {label}")
    if profile_dir is None:
        print("No private profile directory was configured.")
        if scope == "profile":
            print_questions(public_questions)
        else:
            print("Ask for explicit approval for this action; do not infer private permissions or worker policy.")
        return 1

    missing = missing_profile_files(profile_dir) if scope == "profile" else []
    if missing:
        print(f"Missing profile files under: {profile_dir}")
        print(f"Missing: {', '.join(missing)}")
        print_questions(public_questions)
        return 1

    modules = REQUIRED_MODULES if scope == "profile" else REQUIRED_SCOPES[scope]
    unresolved = unresolved_modules(profile_dir, modules)
    profile_file = profile_dir / "PROFILE.md"
    profile_text = profile_file.read_text(encoding="utf-8") if profile_file.is_file() else ""
    if scope == "profile" and "status: complete" not in status_line(profile_text).lower():
        unresolved.setdefault("PROFILE.md", []).append("- status: incomplete")
    if scope == "profile":
        profile_gaps = unresolved_fields(profile_text)
        if "[ ]" in profile_text:
            profile_gaps.append("unchecked module")
        if profile_gaps:
            unresolved["PROFILE.md"] = profile_gaps

    print(f"Profile: {profile_dir}")
    for name, fields in unresolved.items():
        print(f"Unresolved {name}: {', '.join(fields)}")
    if scope == "profile":
        print_questions(profile_dir / "PROFILE-QUESTIONS.md")
    else:
        print("Resolve only this execution boundary or provide a one-time explicit approval.")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a private MinimalShip profile")
    parser.add_argument(
        "--profile-dir",
        type=Path,
        help="Private profile directory; defaults to MINIMALSHIP_PROFILE_DIR or PI_CODING_AGENT_DIR/profile",
    )
    parser.add_argument(
        "--require",
        choices=("profile", "permissions", "orchestration", "dispatch"),
        help=(
            "Require a complete profile or only the execution policy needed for a risky action; "
            "without this option neutral defaults are allowed"
        ),
    )
    args = parser.parse_args()

    profile_dir = resolve_profile_dir(args.profile_dir)
    public_questions = Path(__file__).resolve().parents[1] / "templates" / "profile" / "PROFILE-QUESTIONS.md"

    if profile_dir is None or not profile_dir.exists():
        if args.require:
            return blocked(args.require, profile_dir, public_questions)
        print("PASS: PROFILE_OPTIONAL")
        print("No private profile configured; use neutral defaults.")
        return 0

    if args.require:
        if args.require == "profile":
            profile_text = (profile_dir / "PROFILE.md").read_text(encoding="utf-8") if (profile_dir / "PROFILE.md").is_file() else ""
            profile_incomplete = (
                bool(missing_profile_files(profile_dir))
                or "status: complete" not in status_line(profile_text).lower()
                or bool(unresolved_fields(profile_text))
                or "[ ]" in profile_text
                or bool(unresolved_modules(profile_dir, REQUIRED_MODULES))
            )
            return blocked(args.require, profile_dir, public_questions) if profile_incomplete else _report_required_ready(args.require, profile_dir)
        policy_gaps = unresolved_modules(profile_dir, REQUIRED_SCOPES[args.require])
        missing_policy = any(not (profile_dir / name).is_file() for name in REQUIRED_SCOPES[args.require])
        return blocked(args.require, profile_dir, public_questions) if policy_gaps or missing_policy else _report_required_ready(args.require, profile_dir)

    missing = missing_profile_files(profile_dir)
    if missing:
        print("PASS: PROFILE_PARTIAL")
        print("Private profile is incomplete; use neutral defaults for unresolved preferences.")
        print(f"Profile: {profile_dir}")
        print(f"Missing: {', '.join(missing)}")
        return 0

    profile_text = (profile_dir / "PROFILE.md").read_text(encoding="utf-8")
    unresolved = unresolved_fields(profile_text)
    if "status: complete" not in status_line(profile_text).lower() or unresolved or "[ ]" in profile_text:
        print("PASS: PROFILE_PARTIAL")
        print("Private profile is incomplete; use neutral defaults for unresolved preferences.")
        print(f"Profile: {profile_dir}")
        return 0

    module_gaps = unresolved_modules(profile_dir, REQUIRED_MODULES)
    if module_gaps:
        print("PASS: PROFILE_PARTIAL")
        print("Private profile has unresolved preference fields; use neutral defaults where needed.")
        print(f"Profile: {profile_dir}")
        return 0

    print("PASS: PROFILE_COMPLETE")
    print(f"Profile: {profile_dir}")
    return 0


def _report_required_ready(scope: str, profile_dir: Path) -> int:
    label = "PROFILE_COMPLETE" if scope == "profile" else f"{scope.upper()}_READY"
    print(f"PASS: {label}")
    print(f"Profile: {profile_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
