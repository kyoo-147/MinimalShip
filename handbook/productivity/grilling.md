# Grilling

## What it does

Run a reusable decision-frontier interview that exposes hidden product and architecture assumptions. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `grilling` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a task has unresolved consequential choices and a short interview will prevent building the wrong thing.

## Grilling in practice

Maintain a private decision tree. Ask the current frontier in one round, include a recommendation, and wait for the user before opening the next frontier. Facts are researched by the agent; decisions belong to the user.

## Common questions

**Why not ask everything at once?**

Downstream questions depend on upstream decisions. Asking them early creates noise and false certainty.

## It's working if

- Questions arrive in dependency order and the interview ends as soon as the implementation contract is safe.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a task has unresolved consequential choices and a short interview will prevent building the wrong thing. It sits beside grill-me for explicit user invocation and domain-modeling for language that needs to persist, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
