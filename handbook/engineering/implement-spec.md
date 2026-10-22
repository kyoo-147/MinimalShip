# Implement Spec

## What it does

Execute a complete spec as a dependency-aware task graph on one integration branch. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `implement-spec` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs a spec has several independent slices and the team needs controlled parallel execution.

## Implement Spec in practice

This is the graph executor. The lead owns the integration branch, shared contracts, and `RUN.md`; workers own isolated slices. The graph is a coordination aid, not a reason to create agents.

## Common questions

**Does more parallelism make this faster?**

Only when file ownership and interface contracts are independent. Otherwise one focused implementer is safer.

## It's working if

- Ready work is parallelized only where ownership is independent, and integration is verified after each merge.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a spec has several independent slices and the team needs controlled parallel execution. It sits beside to-tickets for graph creation and code-review for integration review, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
