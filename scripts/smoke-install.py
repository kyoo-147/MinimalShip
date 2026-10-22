#!/usr/bin/env python3
"""Exercise the installer boundary and flat Pi skill layout in a temp directory."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"


def promoted_names() -> list[str]:
    names: list[str] = []
    for bucket in ("engineering", "productivity"):
        for skill_dir in sorted((ROOT / "skills" / bucket).iterdir()):
            if (skill_dir / "SKILL.md").is_file():
                names.append(skill_dir.name)
    return names


def run_install(profile_dir: Path, *, force: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(INSTALLER), "--profile", str(profile_dir)]
    if force:
        command.append("--force")
    return subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    names = promoted_names()
    if len(names) != 27:
        fail(f"expected 27 promoted skills, found {len(names)}")

    with tempfile.TemporaryDirectory(prefix="minimalship-install-") as directory:
        profile_dir = Path(directory)
        first = run_install(profile_dir)
        if first.returncode != 0:
            fail(f"first install failed:\n{first.stdout}{first.stderr}")

        skills_dir = profile_dir / "skills"
        expected = ["minimalship", *names]
        missing = [name for name in expected if not (skills_dir / name / "SKILL.md").is_file()]
        if missing:
            fail(f"flat install is missing skill directories: {', '.join(missing)}")
        if (skills_dir / "minimalship" / "AGENTS.md").exists() or (skills_dir / "minimalship" / "RUN.md").exists():
            fail("root governance or run files crossed the install boundary")
        if list(skills_dir.glob(".minimalship-staging-*")):
            fail("staging directories were not cleaned up")

        sentinel = skills_dir / "implement" / "sentinel.txt"
        sentinel.write_text("must survive a conflict check", encoding="utf-8")
        conflict = run_install(profile_dir)
        if conflict.returncode == 0:
            fail("installer replaced an existing install without --force")
        if not sentinel.is_file():
            fail("conflict check modified an existing skill before --force")

        forced = run_install(profile_dir, force=True)
        if forced.returncode != 0:
            fail(f"forced install failed:\n{forced.stdout}{forced.stderr}")
        if sentinel.exists():
            fail("--force did not replace the conflicting skill directory")

    print("PASS: installer creates root plus 27 flat promoted skills and protects conflicts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
