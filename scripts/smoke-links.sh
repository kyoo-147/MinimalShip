#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
linker="$root/scripts/link-skills.sh"
target="$(mktemp -d -t minimalship-links.XXXXXX)"
trap 'rm -rf -- "$target"' EXIT

bash "$linker" --check "$target" >/dev/null
bash "$linker" "$target" >/dev/null
for name in minimalship implement prototype grill-me; do
  test -f "$target/$name/SKILL.md"
done

printf 'sentinel' > "$target/implement/sentinel.txt"
conflict_output="$target/conflict.log"
if bash "$linker" "$target" >"$conflict_output" 2>&1; then
  echo "FAIL: link helper replaced an existing path without --force" >&2
  exit 1
fi
grep -q 'no links changed' "$conflict_output"
test -f "$target/implement/sentinel.txt"

bash "$linker" --force "$target" >/dev/null
test ! -e "$target/implement/sentinel.txt"
printf 'PASS: link helper checks conflicts and replaces only with --force\n'
