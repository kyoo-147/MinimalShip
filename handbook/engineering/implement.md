# Implement

## What it does

Build one accepted product slice from a spec or bounded work item and close it with evidence. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `implement` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs a single slice is understood and ready to implement on the current branch or worktree.

## Implement in practice

Implementation is a feedback loop, not a ticket-closing ceremony. Keep the change focused, run fast checks while coding, and do not claim completion until the real path and failure case have been exercised.

## Common questions

**Should implementation start with a large architecture pass?**

No. Start with the smallest vertical path and deepen only where current evidence demands it.

## It's working if

- The user journey runs, the relevant checks execute, and the branch reports limitations honestly.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a single slice is understood and ready to implement on the current branch or worktree. It sits beside tdd for behavior seams and code-review for the final branch review, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
