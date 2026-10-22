# Grill Me

## What it does

Interview the user about a product or design until the consequential decisions are explicit. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `grill-me` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs the user explicitly asks to be grilled or the plan contains several product decisions they must own.

## Grill Me in practice

Ask one frontier round at a time. Give a recommended answer so a simple yes can move forward. Stop when the acceptance contract is clear; do not prolong the interview to create certainty about low-risk details.

## Common questions

**Does this replace repository inspection?**

No. The agent should inspect facts itself and ask the user only for decisions, preferences, and authority.

## It's working if

- The interview closes with a shared outcome and no high-risk branch left implicit.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the user explicitly asks to be grilled or the plan contains several product decisions they must own. It sits beside grilling for the reusable interview discipline and grill-with-docs for repository records, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
