# To Spec

## What it does

Turn an already-discussed product request into a compact, testable specification without restarting discovery. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `to-spec` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs the conversation contains enough decisions to write behavior, scope, and acceptance.

## To Spec in practice

A good spec is a compression step. It turns prose into one outcome, a small must-have boundary, observable acceptance, constraints, and a demo command. It does not prescribe implementation details that the codebase can decide.

## Common questions

**Does this interview the user again?**

No. It synthesizes known decisions and marks unresolved high-risk points as blocked.

## It's working if

- The spec names real inputs, outputs, non-goals, and acceptance checks that an implementer can execute.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the conversation contains enough decisions to write behavior, scope, and acceptance. It sits beside grill-with-docs when decisions are missing and to-tickets when the spec is too large for one slice, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
