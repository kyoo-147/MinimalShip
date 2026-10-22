# Diagnosing Bugs

## What it does

Use a disciplined reproduce, minimize, instrument, fix, and regression-test loop for hard bugs and performance regressions. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `diagnosing-bugs` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a report is intermittent, slow, environment-dependent, or not explained by the first stack trace.

## Diagnosing Bugs in practice

The loop is red on the real symptom, minimize inputs and timing, state competing hypotheses, add the least invasive instrumentation, fix the invariant, and rerun the original plus variant cases.

## Common questions

**Can I start by changing the obvious line?**

Only after a reproducer or strong evidence connects that line to the failure. Otherwise the change is a guess.

## It's working if

- A small reproducer distinguishes the failing behavior from nearby hypotheses before the fix is attempted.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a report is intermittent, slow, environment-dependent, or not explained by the first stack trace. It sits beside triage for deciding whether a report is ready and tdd for the regression seam, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
