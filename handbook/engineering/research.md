# Research

## What it does

Investigate a product or engineering question using high-trust sources and a concise evidence-linked note. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `research` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs an external fact, API behavior, ecosystem choice, or user problem needs verification before a decision.

## Research in practice

Prefer primary documentation, source code, standards, and reproducible experiments. Store detailed research in local-only paths when it contains private project context; commit only reusable public guidance.

## Common questions

**Is a collection of links enough?**

No. Each important claim needs a source, date or version context, and a consequence for the decision.

## It's working if

- The note distinguishes observed facts, interpretation, unknowns, and the decision they support.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

an external fact, API behavior, ecosystem choice, or user problem needs verification before a decision. It sits beside prototype for executable uncertainty and to-spec for turning evidence into a contract, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
