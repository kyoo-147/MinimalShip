# To Questionnaire

## What it does

Turn an unresolved decision into a compact questionnaire that another person can answer asynchronously. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `to-questionnaire` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs the agent cannot make a product, legal, operational, or ownership decision and the responsible person is unavailable.

## To Questionnaire in practice

State what is known, what cannot be inferred, and why the answer matters. Make replies easy to paste back into the work record. Keep irreversible or authority-bound decisions visible.

## Common questions

**Is a questionnaire a dump of every possible question?**

No. It should ask only questions that block the next safe action.

## It's working if

- Each question has context, options where useful, a recommended answer, and a clear consequence.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the agent cannot make a product, legal, operational, or ownership decision and the responsible person is unavailable. It sits beside grill-me for a live interview and handoff for transferring an already settled context, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
