# Release checklist

- `python scripts/check.py` passes.
- `bash scripts/list-skills.sh` lists every promoted skill.
- `node scripts/sync-plugin-version.mjs --check` passes.
- Installer smoke tests pass in a disposable target, including flat sibling discovery and conflict protection.
- Link helper smoke tests pass in a disposable target; it runs in conflict-check mode and replaces paths only with an explicit `--force`.
- Private profile smoke test passes for both incomplete and completed first-run states.
- No local-only or removed paths are tracked.
- Public Markdown is original English and links resolve.
- Diff review finds no secrets, copied sources, unnecessary generated noise, or scope drift.
- Conventional Commit and pull request are created from a focused branch.
- Required CI and human review pass before merge.
- The merged result is verified on the integration branch.
