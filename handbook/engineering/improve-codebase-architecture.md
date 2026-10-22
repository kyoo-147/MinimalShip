# Improve Codebase Architecture

## What it does

Survey a codebase for high-leverage module deepening opportunities and turn one selected opportunity into an actionable change. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `improve-codebase-architecture` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs periodic architecture maintenance or a feature that exposes a shallow, leaky, or hard-to-test seam.

## Improve Codebase Architecture in practice

Inspect callers, dependencies, change frequency, test seams, and information leakage. Rank opportunities by current pain and leverage. Keep the report local when it contains repository details.

## Common questions

**Does this produce a full architecture rewrite?**

No. It is a survey and prioritization step. The selected change still needs its own spec and acceptance.

## It's working if

- The review identifies a small number of evidence-backed candidates rather than proposing a rewrite.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

periodic architecture maintenance or a feature that exposes a shallow, leaky, or hard-to-test seam. It sits beside codebase-design for seam vocabulary and retro for environment-level improvements, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
