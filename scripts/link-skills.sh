#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${1:-$HOME/.pi/agent/skills}"
mkdir -p "$target"

while IFS= read -r skill_dir; do
  name="$(basename "$skill_dir")"
  destination="$target/$name"
  rm -rf "$destination"
  ln -s "$skill_dir" "$destination"
  printf 'Linked %-24s -> %s\n' "$name" "$destination"
done < <(find "$root/skills" -mindepth 3 -maxdepth 3 -type f -name SKILL.md -printf '%h\n' | sort)
