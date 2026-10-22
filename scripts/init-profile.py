#!/usr/bin/env python3
"""Create a blank private MinimalShip profile without importing personal data."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

PROFILE_TEMPLATE_DIR = "templates/profile"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create blank private profile templates for a separate MinimalShip agent profile"
    )
    parser.add_argument(
        "--agent-dir",
        type=Path,
        default=Path.home() / ".pi" / "profiles" / "minimalship",
        help="Separate Pi agent directory that will contain a profile/ directory",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing profile template files, without deleting other files",
    )
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1] / PROFILE_TEMPLATE_DIR
    if not source.is_dir():
        raise SystemExit(f"Missing profile template directory: {source}")

    agent_dir = args.agent_dir.expanduser().resolve()
    destination = agent_dir / "profile"
    destination.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0
    for template in sorted(source.iterdir()):
        if not template.is_file():
            continue
        target = destination / template.name
        if target.exists() and not args.overwrite:
            skipped += 1
            continue
        shutil.copy2(template, target)
        copied += 1

    print(f"Profile directory: {destination}")
    print(f"Templates copied: {copied}; existing files kept: {skipped}")
    print("No personal data, credentials, downloads or runtime settings were imported.")
    print(f"Set PI_CODING_AGENT_DIR to: {agent_dir}")
    print(f"Set MINIMALSHIP_PROFILE_DIR to: {destination}")
    print("Answer PROFILE-QUESTIONS.md before using personal preferences.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
