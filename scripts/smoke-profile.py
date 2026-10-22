#!/usr/bin/env python3
"""Exercise optional profile defaults and execution-policy gates."""

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


def fill_template(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^(-\s+[^:\n]+):\s*\?$", r"\1: test value", text, flags=re.MULTILINE)
    text = re.sub(r"^(-\s+[^:\n]+):\s*$", r"\1: test value", text, flags=re.MULTILINE)
    text = re.sub(r"^(\s*\d+\.)\s*\?$", r"\1 test value", text, flags=re.MULTILINE)
    text = text.replace("- status: incomplete", "- status: complete")
    text = text.replace("- [ ]", "- [x]")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="minimalship-profile-") as directory:
        agent_dir = Path(directory)
        initialized = run([sys.executable, str(INIT), "--agent-dir", str(agent_dir)])
        if initialized.returncode != 0:
            fail(f"profile initialization failed:\n{initialized.stdout}{initialized.stderr}")

        profile_dir = agent_dir / "profile"
        optional = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir)])
        if optional.returncode != 0 or "PASS: PROFILE_PARTIAL" not in optional.stdout:
            fail(f"incomplete optional profile did not use neutral defaults:\n{optional.stdout}{optional.stderr}")

        strict = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir), "--require", "profile"])
        if strict.returncode != 1 or "BLOCKED: PROFILE_INCOMPLETE" not in strict.stdout:
            fail(f"explicit full-profile requirement did not block:\n{strict.stdout}{strict.stderr}")

        permissions = run(
            [sys.executable, str(STATUS), "--profile-dir", str(profile_dir), "--require", "permissions"]
        )
        if permissions.returncode != 1 or "BLOCKED: PERMISSIONS_UNRESOLVED" not in permissions.stdout:
            fail(f"permission gate did not isolate the relevant missing policy:\n{permissions.stdout}{permissions.stderr}")

        for path in profile_dir.glob("*.md"):
            if path.name != "PROFILE-QUESTIONS.md":
                fill_template(path)

        opinions = profile_dir / "OPINIONS.md"
        opinions_text = opinions.read_text(encoding="utf-8").replace("1. test value", "1. ?", 1)
        opinions.write_text(opinions_text, encoding="utf-8")
        numbered_gap = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir), "--require", "profile"])
        if numbered_gap.returncode != 1 or "1. ?" not in numbered_gap.stdout:
            fail(f"numbered profile placeholders were not detected:\n{numbered_gap.stdout}{numbered_gap.stderr}")
        fill_template(opinions)

        complete = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir), "--require", "profile"])
        if complete.returncode != 0 or "PASS: PROFILE_COMPLETE" not in complete.stdout:
            fail(f"completed profile was rejected:\n{complete.stdout}{complete.stderr}")

        dispatch = run(
            [sys.executable, str(STATUS), "--profile-dir", str(profile_dir), "--require", "dispatch"]
        )
        if dispatch.returncode != 0 or "PASS: DISPATCH_READY" not in dispatch.stdout:
            fail(f"completed execution policy was rejected:\n{dispatch.stdout}{dispatch.stderr}")

        profile_complete = run([sys.executable, str(STATUS), "--profile-dir", str(profile_dir)])
        if profile_complete.returncode != 0 or "PASS: PROFILE_COMPLETE" not in profile_complete.stdout:
            fail(f"completed profile status was not reported:\n{profile_complete.stdout}{profile_complete.stderr}")

        absent = run([sys.executable, str(STATUS), "--profile-dir", str(agent_dir / "absent")])
        if absent.returncode != 0 or "PASS: PROFILE_OPTIONAL" not in absent.stdout:
            fail(f"missing profile did not allow neutral defaults:\n{absent.stdout}{absent.stderr}")

    print("PASS: profile defaults remain optional while explicit profile and execution gates stay scoped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
