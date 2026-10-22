# Codebase Design

## What it does

Design deep modules and testable seams by hiding complexity behind small, honest interfaces. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `codebase-design` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a module boundary, public interface, or abstraction is difficult to name, test, or change.

## Codebase Design in practice

Use seam, depth, information hiding, locality, leverage, adapter, and representation as design vocabulary. Ask what knowledge is being forced into callers and which invariant can move behind the boundary.

## Common questions

**Is a smaller API always better?**

No. A deep module hides complexity without leaking the decisions callers still need to make.

## It's working if

- The interface gets smaller while the module absorbs more policy and callers know less representation detail.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a module boundary, public interface, or abstraction is difficult to name, test, or change. It sits beside domain-modeling for business language and tdd for testing the chosen seam, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
