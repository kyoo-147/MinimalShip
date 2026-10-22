# Wayfinder

## What it does

Plan a large, multi-session product initiative as a map of decisions and bounded delivery slices. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `wayfinder` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs the destination is clear but the path contains unresolved architecture or product decisions across sessions.

## Wayfinder in practice

Keep the map outside the daily run record when it becomes large. Resolve one decision at a time, update the dependency edges, and convert only settled decisions into implementation tickets.

## Common questions

**Is this a roadmap?**

No. It is a temporary decision map for reaching a specific destination, not a promise to build every idea on it.

## It's working if

- The map shrinks as decisions become evidence-backed tickets, with no hidden architecture work.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the destination is clear but the path contains unresolved architecture or product decisions across sessions. It sits beside grill-with-docs for individual decisions and to-tickets for executable slices, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
