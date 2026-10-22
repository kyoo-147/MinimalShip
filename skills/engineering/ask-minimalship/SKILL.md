---
name: ask-minimalship
description: Choose the smallest MinimalShip flow for a product-development task.
disable-model-invocation: true
---

# Ask MinimalShip

Use this router when a request could follow more than one product-development path.

## Route by need

- Unclear outcome or competing options: use `grill-me` or `grill-with-docs`.
- A settled conversation needs a concise contract: use `to-spec`.
- A large contract needs dependency-aware slices: use `to-tickets`.
- A runnable increment needs building: use `implement` or `implement-spec`.
- A failure is reported: use `diagnosing-bugs`.
- The right module boundary is uncertain: use `codebase-design`.
- Tests need a behavior-first loop: use `tdd`.
- A branch needs independent review: use `code-review`, then `pr`.
- A decision needs several sessions: use `wayfinder`.
- The work is complete and the environment should improve: use `retro`.

Do not route by fashion. Route by the next unresolved decision and the smallest artifact that can settle it. Never invoke two competing orchestration flows for the same task.

When the request is a new project or an existing repository to investigate, route through understanding and planning first: inspect the project, update `FEATURES.md` and `RUN.md`, present the execution proposal, and wait for approval unless the user's original instruction already authorizes implementation. Do not dispatch workers as a side effect of routing.
