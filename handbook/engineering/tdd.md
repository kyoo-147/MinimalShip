# TDD

## What it does

Use a behavior-first red, green, refactor loop at agreed public seams. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `tdd` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a feature or bug has a stable behavior boundary and tests will reduce implementation risk.

## TDD in practice

Test public behavior, not private structure. Work vertically one slice at a time. Keep expected values independent from the implementation and use mocks only at true external boundaries.

## Common questions

**Does every edit require strict TDD?**

No. Use it where feedback and regression risk justify the loop; do not add ritual to trivial configuration changes.

## It's working if

- A failing test states user behavior, the smallest implementation turns it green, and refactoring preserves the contract.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a feature or bug has a stable behavior boundary and tests will reduce implementation risk. It sits beside codebase-design for choosing the seam and code-review for refactoring after behavior is protected, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
