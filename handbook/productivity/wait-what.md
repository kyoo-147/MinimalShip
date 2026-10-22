# Wait, What?

## What it does

Repair a misunderstanding by restating the request in the project's vocabulary and checking the smallest disputed point. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `wait-what` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs the user's message, the agent's proposal, or a product term clearly did not land.

## Wait, What? in practice

Stop the current trajectory. State what you think the user wants, what you may have misunderstood, and one concrete example. Ask for correction before adding scope or code.

## Common questions

**Should this be used whenever the user is brief?**

No. Use it when there is evidence of a mismatch, not as a preamble to every request.

## It's working if

- The restatement is shorter, concrete, and accepted before more work is done.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the user's message, the agent's proposal, or a product term clearly did not land. It sits beside domain-modeling for stable vocabulary and grilling for unresolved decisions, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
