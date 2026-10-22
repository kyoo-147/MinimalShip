# Retro

## What it does

Review a completed coding session and propose the smallest environment improvement with evidence. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `retro` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs repeated friction, preventable mistakes, or missing feedback loops appeared during a session.

## Retro in practice

Trace the session from request to evidence. Separate product ambiguity, code design, environment setup, and agent behavior. Recommend one severe fix first, then leave lower-impact ideas in a bounded backlog.

## Common questions

**Does every awkward moment become a new rule?**

No. Record only repeated or high-cost friction with a practical prevention.

## It's working if

- The retro produces a short, prioritized change to tools, instructions, tests, or workflow, not a mood report.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

repeated friction, preventable mistakes, or missing feedback loops appeared during a session. It sits beside handoff for continuity and improve-codebase-architecture for code design problems, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
