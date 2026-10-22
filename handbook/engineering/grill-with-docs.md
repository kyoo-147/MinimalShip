# Grill With Docs

## What it does

Resolve consequential product and architecture ambiguity while maintaining the project's vocabulary and decision records. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `grill-with-docs` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs a high-ambiguity change where terminology, trade-offs, or durable decisions affect implementation.

## Grill With Docs in practice

This is the documented version of a grill. It asks only the current decision frontier, writes accepted vocabulary to `GLOSSARY.md` when useful, and adds an ADR only when the decision has lasting architectural weight.

## Common questions

**Will this always create an ADR?**

No. Record only decisions that are hard to reverse or that future agents would otherwise rediscover.

## It's working if

- The final contract names the user journey, boundaries, risks, and decisions without a large speculative PRD.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a high-ambiguity change where terminology, trade-offs, or durable decisions affect implementation. It sits beside grill-me for a stateless interview and domain-modeling for terminology work, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
