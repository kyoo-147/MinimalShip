# To Tickets

## What it does

Break a product spec into small tracer-bullet work items with explicit dependency edges and acceptance checks. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `to-tickets` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs a spec is larger than one safe implementation slice or needs bounded parallel ownership.

## To Tickets in practice

Tickets are not a substitute for a product goal. Split at user-visible or independently verifiable seams, keep interfaces explicit, and leave optional ideas outside the current graph.

## Common questions

**Is this a backlog generator?**

No. It creates only the smallest work graph needed to reach the accepted outcome.

## It's working if

- Every ticket has one output, one owner, one check, and a visible dependency edge.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a spec is larger than one safe implementation slice or needs bounded parallel ownership. It sits beside to-spec for the source contract and implement-spec for executing the resulting graph, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
