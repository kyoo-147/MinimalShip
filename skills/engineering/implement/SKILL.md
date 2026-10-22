---
name: implement
description: Build one accepted product slice from a spec or bounded work item and close it with evidence.
disable-model-invocation: true
---

# Implement

1. Pin the accepted spec or work item and confirm the current branch.
2. Read the relevant code, tests, glossary, ADRs, and package scripts.
3. Choose the smallest public seam and call `tdd` when tests improve confidence.
4. Implement a vertical slice with no unrelated refactor or dependency.
5. Run focused tests, typechecks, lint, build, and one realistic smoke path as applicable.
6. Review the diff for scope, secrets, regressions, and missing acceptance evidence.
7. Call `code-review` before committing when the change is more than trivial.

Report PASS, FAIL, or BLOCKED per acceptance case. A successful compile is not proof of a working product.
