# Handoff

## What it does

Compress the current session into an evidence-linked handoff another agent can resume safely. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `handoff` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs context is running out, ownership is moving, or another agent must continue without replaying the whole conversation.

## Handoff in practice

Write a compact handoff under the repository's local-only analysis path unless the user explicitly wants a committed document. Include exact paths, branch, tests, unresolved choices, and the smallest next step.

## Common questions

**Should a handoff include every chat message?**

No. Preserve decisions and evidence, not transcript noise.

## It's working if

- The next agent knows the goal, decisions, current files, commands, blockers, and next action without guesswork.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

context is running out, ownership is moving, or another agent must continue without replaying the whole conversation. It sits beside retro for improving the workflow and to-spec for converting settled context into a build contract, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
