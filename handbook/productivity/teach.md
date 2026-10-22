# Teach

## What it does

Teach a product-development concept through a small sequence of explanations, exercises, and verified practice. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `teach` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs the user wants to build durable understanding rather than receive a one-off answer.

## Teach in practice

Use the current workspace as a stateful learning notebook when the user wants that. Alternate explanation, a concrete exercise, feedback, and a short recap. Avoid turning the repository into an unrelated curriculum.

## Common questions

**Does teaching mean writing a long course?**

No. Start with the smallest concept that unlocks the current decision and expand only when practice exposes a gap.

## It's working if

- The learner can explain the concept, apply it to the current product, and identify a next practice step.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the user wants to build durable understanding rather than receive a one-off answer. It sits beside research for source gathering and handoff for preserving learning progress, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
