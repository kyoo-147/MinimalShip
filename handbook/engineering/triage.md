# Triage

## What it does

Move product and engineering reports through a small evidence-based state machine. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `triage` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs an issue, bug report, or external pull request needs classification before implementation.

## Triage in practice

Use a state machine such as needs-evidence, verified, ready, blocked, declined, or shipped. Keep labels and tracker mechanics configurable. The state is less important than the evidence that justifies moving it.

## Common questions

**Does triage decide priority by intuition?**

No. It records impact, evidence, uncertainty, and the smallest useful next step.

## It's working if

- Each item ends with a clear state, evidence, owner, and next action instead of a vague priority label.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

an issue, bug report, or external pull request needs classification before implementation. It sits beside diagnosing-bugs for reproducing a confirmed bug and to-tickets for ready work, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
