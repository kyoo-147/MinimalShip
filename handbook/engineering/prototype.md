# Prototype

## What it does

Build a disposable prototype to answer one product, state, interaction, or architecture question. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `prototype` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a decision is cheaper to test by running a small artifact than by debating it in the abstract.

## Prototype in practice

Set a question, a timebox, a falsifiable observation, and a discard rule. Build only the path needed to observe the decision. Do not polish a prototype into a hidden product.

## Common questions

**Can prototype code go straight to production?**

Only after a separate implementation pass checks security, maintainability, tests, and scope.

## It's working if

- The prototype answers a named question and is either discarded or deliberately promoted with a new contract.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a decision is cheaper to test by running a small artifact than by debating it in the abstract. It sits beside grilling for the question and implement for production work after the decision, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
