# Code Review

## What it does

Review a diff on standards and product-spec axes, with separate evidence for correctness, scope, and design risk. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `code-review` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a branch, pull request, or fix needs an independent review before commit or merge.

## Code Review in practice

Pin a fixed point, read the originating spec, and review standards and spec independently. Prefer findings that a maintainer can act on. Do not use review as a license for unrelated cleanup.

## Common questions

**Is a green test suite enough?**

No. Review also checks scope, acceptance, security, regressions, maintainability, and unnecessary complexity.

## It's working if

- The review names concrete findings by file and separates required fixes from judgment calls.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a branch, pull request, or fix needs an independent review before commit or merge. It sits beside tdd for behavior evidence and pr for the final human-facing delivery summary, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
