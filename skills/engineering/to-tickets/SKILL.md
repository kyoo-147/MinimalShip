---
name: to-tickets
description: Break a product spec into small tracer-bullet work items with explicit dependency edges and acceptance checks.
disable-model-invocation: true
---

# To Tickets

- Start from the acceptance cases, not a list of imagined technical tasks.
- Create a runnable skeleton first when the system is new.
- Give each ticket one vertical result and one acceptance check.
- Mark blocking edges explicitly: contract, schema, environment, or prior slice.
- Assign a path or worktree boundary so parallel workers cannot edit the same mutable file.
- Keep a single owner for shared interfaces and manifests.
- Prefer a local Markdown table when no issue tracker is configured.

A ticket is ready only when an implementer can start without asking what "done" means.

Keep the resulting task IDs and ownership in `RUN.md`; update the corresponding rows in `FEATURES.md` only when a feature status changes. Do not create a second task tracker.
