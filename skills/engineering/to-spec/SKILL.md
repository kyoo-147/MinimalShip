---
name: to-spec
description: Turn an already-discussed product request into a compact, testable specification without restarting discovery.
disable-model-invocation: true
---

# To Spec

1. Read the current conversation, repository rules, existing work records, and relevant code.
2. Extract the user, problem, desired outcome, constraints, and evidence already agreed.
3. Write one primary outcome and a short MUST / NOT NOW boundary.
4. Add three to seven acceptance cases in input -> action -> expected result form.
5. Add failure behavior, permissions, and a real demo or smoke command.
6. Update `FEATURES.md` for the requested feature or the existing verified capability it changes, keeping origin and status distinct.
7. Update `RUN.md` with the current objective, scope, acceptance evidence and open decisions.
8. List assumptions explicitly. If one changes the design materially, stop and ask rather than guessing.

Write the result to the repository's chosen work record or configured tracker. Keep the spec implementation-neutral but executable.
