# MinimalShip repository conventions

This repository is a composable product-development skill bundle. Read `AGENTS.md` before changing it.

## Promotion contract

Every promoted skill under `skills/engineering/` or `skills/productivity/` must have:

- `SKILL.md` with `name` and `description` frontmatter
- `agents/openai.yaml` with display metadata
- matching invocation policy in both files
- a page under `handbook/<bucket>/<name>.md`
- an entry in the bucket README and root README
- an entry in `.claude-plugin/plugin.json`

The `scripts/check.py` checker is the source of truth for this contract. Run it after adding, removing, renaming, or changing a promoted skill.

## Invocation

User-invoked skills are explicit commands such as routers, setup, interviewing, planning, and implementation. Model-invoked skills are reusable disciplines such as testing, diagnosis, design, review, and research. Do not make a user-invoked skill depend on another user-invoked skill.

## Public content

Write public guidance in original English. Keep product-development scope only. Preserve useful ideas from the supplied MinimalShip v0.3 bundle, including Quick/Deep grilling, output contracts, performance criteria, anti-overengineering boundaries, and truthful status reporting. Do not copy third-party prose or publish the raw sources used for research.

## Documentation boundary

`docs/`, `analysis/`, and `.local/` are private working areas and ignored by Git. Use `handbook/` for public human-facing pages. Do not weaken the ignore rule merely to add repository docs.

## Release and validation

Keep `package.json` and `.claude-plugin/plugin.json` versions synchronized. Run:

```bash
python scripts/check.py
bash scripts/list-skills.sh
node scripts/sync-plugin-version.mjs --check
```

Use `scripts/install.py` for Pi installation. It must not run downloads, hooks, or arbitrary project code.
