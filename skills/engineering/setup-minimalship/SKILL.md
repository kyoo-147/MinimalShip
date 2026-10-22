---
name: setup-minimalship
description: Configure a repository for the MinimalShip product-development workflow without imposing an issue tracker or hosted service.
disable-model-invocation: true
---

# Set Up MinimalShip

Run once before using the larger flow in a new repository.

- Inspect existing `AGENTS.md`, `CLAUDE.md`, `README.md`, tests, and package scripts.
- Preserve existing conventions unless they conflict with truthful acceptance or safety.
- Confirm the product vocabulary and add only terms that affect code or decisions.
- Choose the work record: root `RUN.md`, an existing tracker, or a documented adapter.
- Record the test, typecheck, build, start, and smoke commands that actually exist.
- Record whether Pi, Herdr, worktrees, network calls, installs, cloud dashboards, or deployment are allowed.
- Keep `docs/`, `analysis/`, and `.local/` local-only in this repository.

Do not invent labels, ticket infrastructure, or a hosted service just because another repository uses them.
