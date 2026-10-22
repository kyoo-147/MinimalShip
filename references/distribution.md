# Distribution model

MinimalShip has three layers:

1. The root `SKILL.md` is the Pi-friendly product workflow installed as `/skill:minimalship`.
2. Promoted skills under `skills/engineering` and `skills/productivity` are composable skills for harnesses that support plugin or Agent Skills layouts.
3. `references/`, `templates/`, and the scripts support the root workflow and are copied only when needed.

The repository also carries Claude-style plugin manifests and Codex metadata so compatible harnesses can discover the same promoted set. These manifests do not change Pi's runtime behavior.

The installer never downloads dependencies, runs hooks, copies credentials, or includes local-only `docs/`, `analysis/`, `.local/`, `.pi/`, `.minimalship/`, `.git/`, or repository governance files. Use `scripts/link-skills.sh` only as a maintainer convenience for symlink-capable environments.

## Private profile distribution

The public package includes neutral profile templates and a first-run question catalog.
It does not include a completed operator profile.
Use `scripts/init-profile.py` to create blank files under a separate agent directory, then set `PI_CODING_AGENT_DIR` and `MINIMALSHIP_PROFILE_DIR` when launching Pi.
The installer can place the skill under that separate agent directory with `--profile`.
Profile answers, private paths, credentials and recovery archives stay outside Git.
