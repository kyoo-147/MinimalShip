---
name: handoff
description: Compress the current session into an evidence-linked handoff another agent can resume safely.
disable-model-invocation: true
---

# Handoff

Produce a handoff with:

1. Goal, current cycle and accepted scope from `FEATURES.md` and `RUN.md`.
2. Decisions and their reasons.
3. Files changed or inspected, including the state records.
4. Commands run and factual outcomes.
5. Current branch and working-tree state.
6. Blockers, risks, and unresolved questions.
7. One recommended next action, copied into `RUN.md` when the repository is being handed off.

Do not write secrets or claim work that exists only in a plan. Prefer a short handoff that can be checked against the repository.
