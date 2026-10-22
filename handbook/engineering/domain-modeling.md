# Domain Modeling

## What it does

Build a shared product vocabulary and keep code, acceptance, and decisions aligned with it. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `domain-modeling` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs the same concept has several names, a rule is hidden in incidental code, or a feature crosses a domain boundary.

## Domain Modeling in practice

Challenge terms against real examples and edge cases. Prefer one precise term over a list of synonyms. Record only language that reduces future ambiguity.

## Common questions

**Is a glossary just documentation?**

No. It is useful when it changes names, boundaries, tests, or decisions in the codebase.

## It's working if

- A reader can explain the important nouns, states, and transitions without translating between documents and code.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

the same concept has several names, a rule is hidden in incidental code, or a feature crosses a domain boundary. It sits beside grilling for user decisions and codebase-design for module placement, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
