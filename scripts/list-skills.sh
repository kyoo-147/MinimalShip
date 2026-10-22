#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
while IFS= read -r skill; do
  name="$(basename "$(dirname "$skill")")"
  description="$(awk 'BEGIN{inside=0} /^---$/{inside=!inside; next} inside && /^description:/{sub(/^description:[[:space:]]*/, ""); print; exit}' "$skill")"
  printf '%-34s %s\n' "$name" "$description"
done < <(find "$root/skills" -mindepth 3 -maxdepth 3 -type f -name SKILL.md | sort)
