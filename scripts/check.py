#!/usr/bin/env python3
"""Check MinimalShip skill artifacts and preserved source files."""

import hashlib
import json
from pathlib import Path


def read_text(path: Path, encoding: str) -> str:
    try:
        return path.read_text(encoding=encoding)
    except OSError as exc:
        raise SystemExit(f"Could not read {path}: {exc}") from exc


def read_bytes(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise SystemExit(f"Could not read {path}: {exc}") from exc


def load_manifest(path: Path) -> dict[str, str]:
    try:
        return json.loads(read_text(path, "utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skill_path = root / "SKILL.md"
    template_path = root / "templates" / "RUN.md"
    manifest_path = root / "sources" / "SHA256.json"
    index_path = root / "references" / "complete-line-index.md"

    if not skill_path.is_file() or not template_path.is_file():
        raise SystemExit("Missing required MinimalShip skill artifact")

    skill = read_text(skill_path, "utf-8")
    required = ("ASK", "DISPATCH", "VERIFY")
    if not skill.startswith("---\nname: minimalship\n") or any(
        marker not in skill for marker in required
    ):
        raise SystemExit("SKILL.md has an invalid MinimalShip skill header or workflow")

    manifest = load_manifest(manifest_path)
    index = read_text(index_path, "utf-8")
    for name, expected in manifest.items():
        source_path = root / "sources" / name
        digest = hashlib.sha256(read_bytes(source_path)).hexdigest()
        if digest != expected:
            raise SystemExit(f"SHA-256 mismatch: {name}")

        lines = read_text(source_path, "utf-8-sig").splitlines()
        if f"SOURCE: {name} (" not in index:
            raise SystemExit(f"Missing source index entry: {name}")
        if f"[{len(lines):04d}]" not in index:
            raise SystemExit(f"Missing source line count: {name}")

    print(
        "PASS: MinimalShip skill structure and all original bytes/line counts verified:",
        len(manifest),
        "unique sources",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
