#!/usr/bin/env python3
"""Exercise the installer boundary, flat Pi layout and rollback behavior."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from types import ModuleType
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"


def load_installer() -> ModuleType:
    spec = importlib.util.spec_from_file_location("minimalship_install", INSTALLER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load installer module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def promoted_names() -> list[str]:
    names: list[str] = []
    for bucket in ("engineering", "productivity"):
        for skill_dir in sorted((ROOT / "skills" / bucket).iterdir()):
            if (skill_dir / "SKILL.md").is_file():
                names.append(skill_dir.name)
    return names


def run_install(target: Path, *, kind: str, force: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(INSTALLER), f"--{kind}", str(target)]
    if force:
        command.append("--force")
    return subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)


def fail(message: str) -> NoReturn:
    raise SystemExit(f"FAIL: {message}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"could not read {path}: {exc}")


def assert_flat_install(skills_dir: Path, names: list[str]) -> None:
    expected = ["minimalship", *names]
    missing = [name for name in expected if not (skills_dir / name / "SKILL.md").is_file()]
    if missing:
        fail(f"flat install is missing skill directories: {', '.join(missing)}")
    if any((skills_dir / "minimalship" / name).exists() for name in ("AGENTS.md", "FEATURES.md", "RUN.md")):
        fail("root governance or project state crossed the install boundary")
    if list(skills_dir.glob(".minimalship-staging-*")):
        fail("staging directories were not cleaned up")


def main() -> int:
    names = promoted_names()
    if len(names) != 27:
        fail(f"expected 27 promoted skills, found {len(names)}")

    installer = load_installer()
    with tempfile.TemporaryDirectory(prefix="minimalship-install-") as directory:
        root = Path(directory)
        profile_dir = root / "profile"
        project_dir = root / "project"

        first = run_install(profile_dir, kind="profile")
        if first.returncode != 0:
            fail(f"profile install failed:\n{first.stdout}{first.stderr}")
        profile_skills = profile_dir / "skills"
        assert_flat_install(profile_skills, names)

        project = run_install(project_dir, kind="project")
        if project.returncode != 0:
            fail(f"project install failed:\n{project.stdout}{project.stderr}")
        assert_flat_install(project_dir / ".pi" / "skills", names)

        unrelated = profile_skills / "unrelated-user-skill"
        unrelated.mkdir()
        unrelated_marker = unrelated / "sentinel.txt"
        unrelated_marker.write_text("must survive MinimalShip installs", encoding="utf-8")

        sentinel = profile_skills / "implement" / "sentinel.txt"
        sentinel.write_text("must survive a conflict check", encoding="utf-8")
        conflict = run_install(profile_dir, kind="profile")
        if conflict.returncode == 0:
            fail("installer replaced an existing install without --force")
        if not sentinel.is_file() or not unrelated_marker.is_file():
            fail("conflict check modified an existing or unrelated skill")

        forced = run_install(profile_dir, kind="profile", force=True)
        if forced.returncode != 0:
            fail(f"forced install failed:\n{forced.stdout}{forced.stderr}")
        if sentinel.exists():
            fail("--force did not replace the conflicting skill directory")
        if not unrelated_marker.is_file():
            fail("--force removed an unrelated skill directory")

        rollback_dir = root / "rollback"
        rollback_skills = rollback_dir / "skills"
        rollback_skills.mkdir(parents=True)
        old_root = rollback_skills / "minimalship"
        old_worker = rollback_skills / "ask-minimalship"
        old_root.mkdir()
        old_worker.mkdir()
        (old_root / "old.txt").write_text("old root", encoding="utf-8")
        (old_worker / "old.txt").write_text("old worker", encoding="utf-8")

        sources = [(installer.SKILL_NAME, ROOT, True)]
        sources.extend((path.name, path, False) for path in installer.promoted_sources(ROOT))
        moves = 0

        def fail_once_mover(source: str, destination: str) -> str | None:
            nonlocal moves
            moves += 1
            if moves == 3:
                raise OSError("injected move failure for rollback smoke test")
            try:
                return shutil.move(source, destination)
            except OSError:
                raise

        try:
            installer.install_skills(ROOT, rollback_skills, sources, force=True, mover=fail_once_mover)
        except SystemExit:
            pass
        else:
            fail("injected install failure unexpectedly succeeded")

        if read_text(old_root / "old.txt") != "old root":
            fail("failed install did not restore the existing root skill")
        if read_text(old_worker / "old.txt") != "old worker":
            fail("failed install did not restore the existing promoted skill")
        if list(rollback_skills.glob(".minimalship-staging-*")):
            fail("failed install left a staging directory")

        fresh_skills = root / "fresh-rollback" / "skills"
        fresh_skills.mkdir(parents=True)
        moves = 0

        def fail_first_mover(source: str, destination: str) -> str | None:
            nonlocal moves
            moves += 1
            if moves == 1:
                raise OSError("injected first-move failure for fresh install")
            try:
                return shutil.move(source, destination)
            except OSError:
                raise

        try:
            installer.install_skills(ROOT, fresh_skills, sources, force=True, mover=fail_first_mover)
        except SystemExit:
            pass
        else:
            fail("fresh injected install failure unexpectedly succeeded")

        if any((fresh_skills / name).exists() for name, _, _ in sources):
            fail("failed fresh install left a partial skill tree")
        if list(fresh_skills.glob(".minimalship-staging-*")):
            fail("failed fresh install left a staging directory")

    print("PASS: installer supports profile/project layouts, preserves unrelated skills, protects conflicts, and restores failed replacements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
