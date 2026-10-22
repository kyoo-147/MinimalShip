# Pull Request

## What it does

Write a concise pull request that explains the user outcome, proof, risk, and merge decision. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `pr` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a branch is ready for human review and needs a truthful, evidence-first handoff.

## Pull Request in practice

Lead with the smallest visual of the change. Include acceptance evidence, tests, risks, deployment notes, and explicit limitations. Call out one-way doors and rollback concerns.

## Common questions

**Should the PR body repeat every implementation detail?**

No. It should make the decision and evidence easy to inspect, not become a second design document.

## It's working if

- A reviewer can understand before/after behavior, checks, risk, and follow-up without reading the whole conversation.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a branch is ready for human review and needs a truthful, evidence-first handoff. It sits beside code-review for findings and implement for the underlying change, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
