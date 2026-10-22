#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/link-skills.sh [--force] [--check] [target]

Link the root MinimalShip skill and all promoted skills into target.
Existing paths are reported and preserved unless --force is supplied.
EOF
}

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="$HOME/.pi/agent/skills"
force=0
check_only=0

while (($# > 0)); do
  case "$1" in
    --force) force=1 ;;
    --check) check_only=1 ;;
    -h|--help) usage; exit 0 ;;
    --) shift; break ;;
    -*) usage >&2; exit 2 ;;
    *) target="$1"; shift; break ;;
  esac
  shift
done

if (($# > 0)); then
  usage >&2
  exit 2
fi

mkdir -p "$target"
skill_dirs=("$root")
skill_names=("minimalship")
while IFS= read -r skill_dir; do
  skill_dirs+=("$skill_dir")
  skill_names+=("$(basename "$skill_dir")")
done < <(find "$root/skills" -mindepth 3 -maxdepth 3 -type f -name SKILL.md -exec dirname {} \; | sort)

destinations=()
conflicts=()
for index in "${!skill_dirs[@]}"; do
  name="${skill_names[$index]}"
  destination="$target/$name"
  destinations+=("$destination")
  if [[ -e "$destination" || -L "$destination" ]]; then
    conflicts+=("$destination")
  fi
done

if ((${#conflicts[@]} > 0 && force == 0)); then
  printf 'Conflicting skill paths; no links changed:\n' >&2
  printf ' - %s\n' "${conflicts[@]}" >&2
  printf 'Re-run with --force to replace them deliberately.\n' >&2
  exit 2
fi

if ((check_only)); then
  printf 'PASS: no link conflicts in %s\n' "$target"
  exit 0
fi

for index in "${!skill_dirs[@]}"; do
  skill_dir="${skill_dirs[$index]}"
  name="${skill_names[$index]}"
  destination="${destinations[$index]}"
  if [[ -e "$destination" || -L "$destination" ]]; then
    rm -rf -- "$destination"
  fi
  ln -s "$skill_dir" "$destination"
  printf 'Linked %-24s -> %s\n' "$name" "$destination"
done
