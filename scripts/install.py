#!/usr/bin/env python3
"""Non-destructive MinimalShip installer with actionable filesystem errors."""

import argparse
import shutil
from pathlib import Path

SKILL_NAME = "minimalship"


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--global",
        dest="global_install",
        action="store_true",
        help="Install into ~/.pi/agent/skills/minimalship",
    )
    group.add_argument(
        "--project",
        type=Path,
        help="Project directory into which .pi/skills/minimalship is installed",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing MinimalShip skill",
    )
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1]
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Invalid MinimalShip source directory: {source}")

    destination = (
        Path.home() / ".pi/agent/skills" / SKILL_NAME
        if args.global_install
        else args.project.expanduser().resolve() / ".pi/skills" / SKILL_NAME
    )
    if source.resolve() == destination.resolve():
        print("Already installed:", destination)
        return 0

    try:
        if destination.exists() or destination.is_symlink():
            if not args.force:
                raise SystemExit(
                    f"Existing skill at {destination}; "
                    "pass --force to replace deliberately"
                )
            if destination.is_dir() and not destination.is_symlink():
                shutil.rmtree(destination)
            else:
                destination.unlink()

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns(
                "__pycache__",
                "*.pyc",
                ".DS_Store",
                ".git",
                ".pi",
                "docs",
                "analysis",
                ".local",
                "AGENTS.md",
            ),
        )
    except OSError as exc:
        raise SystemExit(
            f"Could not install MinimalShip to {destination}: {exc}"
        ) from exc

    print("Installed:", destination)
    print("Open Pi and run /skill:minimalship <task>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
