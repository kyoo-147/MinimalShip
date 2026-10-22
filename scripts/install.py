#!/usr/bin/env python3
"""Install MinimalShip as a Pi root skill plus flat promoted skill siblings."""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path

SKILL_NAME = "minimalship"
PROMOTED_BUCKETS = ("engineering", "productivity")
COMMON_EXCLUDED = {
    ".git",
    ".pi",
    ".minimalship",
    ".local",
    ".github",
    ".changeset",
    ".ruff_cache",
    "node_modules",
    "docs",
    "analysis",
    "__pycache__",
}
ROOT_ONLY_EXCLUDED = {"AGENTS.md", "CLAUDE.md", "RUN.md"}


def ignored(source: Path, *, omit_root_files: bool = False):
    """Return a copytree ignore callback for public distribution boundaries."""

    def ignore(directory: str, names: list[str]) -> set[str]:
        excluded = set(COMMON_EXCLUDED)
        if omit_root_files and Path(directory).resolve() == source.resolve():
            excluded.update(ROOT_ONLY_EXCLUDED)
        return {name for name in names if name in excluded or name.endswith(".pyc")}

    return ignore


def promoted_sources(source: Path) -> list[Path]:
    """Return every promoted skill directory in deterministic order."""

    result: list[Path] = []
    for bucket in PROMOTED_BUCKETS:
        bucket_dir = source / "skills" / bucket
        if not bucket_dir.is_dir():
            raise SystemExit(f"Missing promoted skill bucket: {bucket_dir}")
        for skill_dir in sorted(path for path in bucket_dir.iterdir() if path.is_dir()):
            if (skill_dir / "SKILL.md").is_file():
                result.append(skill_dir)
    return result


def destination_root(args: argparse.Namespace) -> Path:
    if args.global_install:
        return Path.home() / ".pi" / "agent" / "skills"
    if args.project is not None:
        return args.project.expanduser().resolve() / ".pi" / "skills"
    return args.profile.expanduser().resolve() / "skills"


def remove_path(path: Path) -> None:
    try:
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()
    except OSError as exc:
        raise OSError(f"Could not remove existing skill path {path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install MinimalShip into a Pi skill directory with flat promoted siblings"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--global",
        dest="global_install",
        action="store_true",
        help="Install into ~/.pi/agent/skills/{minimalship,<promoted-skill>}",
    )
    group.add_argument(
        "--project",
        type=Path,
        help="Project directory whose .pi/skills directory receives the root and promoted skills",
    )
    group.add_argument(
        "--profile",
        type=Path,
        help="Separate Pi agent/profile directory whose skills directory receives the install",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace conflicting root or promoted skill directories deliberately",
    )
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1]
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Invalid MinimalShip source directory: {source}")

    skill_sources = [(SKILL_NAME, source, True)]
    skill_sources.extend((skill_dir.name, skill_dir, False) for skill_dir in promoted_sources(source))
    names = [name for name, _, _ in skill_sources]
    if len(names) != len(set(names)):
        raise SystemExit("Promoted skill names collide with each other or the root skill")

    skills_dir = destination_root(args)
    root_destination = skills_dir / SKILL_NAME
    if source.resolve() == root_destination.resolve():
        raise SystemExit("Refusing to install into the source checkout; choose a separate Pi skill directory")

    destinations = [skills_dir / name for name in names]
    conflicts = [path for path in destinations if path.exists() or path.is_symlink()]
    if conflicts and not args.force:
        lines = "\n".join(f"- {path}" for path in conflicts)
        raise SystemExit(
            "Existing skill paths found; no files were changed.\n"
            f"{lines}\n"
            "Pass --force to replace these paths deliberately."
        )

    try:
        skills_dir.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-staging-", dir=skills_dir))
    except OSError as exc:
        raise SystemExit(f"Could not prepare install directory {skills_dir}: {exc}") from exc

    moved: list[Path] = []
    try:
        for name, skill_source, is_root in skill_sources:
            shutil.copytree(
                skill_source,
                staging / name,
                ignore=ignored(skill_source, omit_root_files=is_root),
            )

        for destination in destinations:
            if destination.exists() or destination.is_symlink():
                if not args.force:
                    raise SystemExit(f"Install conflict appeared during staging: {destination}")
                remove_path(destination)

        for name, _, _ in skill_sources:
            destination = skills_dir / name
            shutil.move(str(staging / name), str(destination))
            moved.append(destination)
    except (OSError, SystemExit) as exc:
        for destination in reversed(moved):
            if destination.exists() or destination.is_symlink():
                remove_path(destination)
        if isinstance(exc, SystemExit):
            raise
        raise SystemExit(f"Could not install MinimalShip to {skills_dir}: {exc}") from exc
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    print("Installed root skill:", root_destination)
    print(f"Installed promoted skills: {len(skill_sources) - 1}")
    print("Included: flat Pi-discoverable skills, root references, templates, and public metadata")
    if args.profile is not None:
        print("Profile runtime: set PI_CODING_AGENT_DIR to the selected profile directory")
    print("Open Pi and run /skill:minimalship <task> or /skill:<promoted-name>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
