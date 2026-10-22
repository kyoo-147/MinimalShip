# Ask MinimalShip

## What it does

Choose the smallest MinimalShip flow for a product-development task. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `ask-minimalship` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs routing a product request to the right discovery, build, verification, or delivery step.

## Ask MinimalShip in practice

Start with the user's desired outcome, then classify the work as discovery, specification, implementation, diagnosis, review, or release. Prefer the shortest path that still protects acceptance and evidence. If a task crosses boundaries, state the sequence instead of invoking every skill at once.

## Common questions

**Does this replace the other skills?**

No. It is a router. Once the path is clear, use the named skill directly.

## It's working if

- The chosen flow has one owner, one outcome, and no duplicated ceremony.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

routing a product request to the right discovery, build, verification, or delivery step. It sits beside grill-me for an interview and implement for execution, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
