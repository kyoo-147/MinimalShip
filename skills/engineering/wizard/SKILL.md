---
name: wizard
description: Generate a safe interactive shell wizard for steps only a human can complete, such as credentials or provider dashboards.
---

# Wizard

- Name the human-only step and why the agent cannot perform it.
- Show prerequisites, expected outputs, and a safe cancel path.
- Read secrets without echoing them and never write them to the repository.
- Validate provider, environment, target, and irreversible actions before confirmation.
- Print exact next commands and evidence the human should return.
- Keep the script bounded and auditable; do not add a daemon or hidden network call.

For cloud or deployment work, separate preparation, human approval, execution, and verification so a partial run is recoverable.
