#!/usr/bin/env python3
"""Exercise the private profile initializer and first-run gate."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INIT = ROOT / "scripts" / "init-profile.py"
STATUS = ROOT / "scripts" / "profile-status.py"


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="minimalship-profile-") as directory:
        agent_dir = Path(directory)
        initialized = run([sys.executable, str(INIT), "--agent-dir", str(agent_dir)])
        if initialized.returncode != 0:
            fail(f"profile initialization failed:\n{initialized.stdout}{initialized.stderr}")

        profile_dir = agent_dir / "profile"
        blocked = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir)])
        if blocked.returncode != 1 or "BLOCKED: PROFILE_INCOMPLETE" not in blocked.stdout:
            fail("new profile did not stop at the first-run gate")

        profile_file = profile_dir / "PROFILE.md"
        profile_text = profile_file.read_text(encoding="utf-8")
        profile_text = profile_text.replace("- status: incomplete", "- status: complete")
        profile_text = re.sub(r"^(-\s+[^:]+):\s*\?$", r"\1: test value", profile_text, flags=re.MULTILINE)
        profile_text = profile_text.replace("- [ ]", "- [x]")
        profile_file.write_text(profile_text, encoding="utf-8")

        complete = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir)])
        if complete.returncode != 0 or "PASS: PROFILE_COMPLETE" not in complete.stdout:
            fail(f"completed profile was rejected:\n{complete.stdout}{complete.stderr}")

    print("PASS: profile initializer and first-run gate handle incomplete and complete profiles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
