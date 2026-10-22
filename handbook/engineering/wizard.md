# Wizard

## What it does

Generate a safe interactive shell wizard for steps only a human can complete, such as credentials or provider dashboards. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `wizard` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs a deployment, cloud, account, secret, or cutover step requires human authority or a visual third-party UI.

## Wizard in practice

Keep the agent responsible for everything it can safely do. Generate a wizard only for the remainder: login, approval, secret entry, dashboard choice, or irreversible cutover.

## Common questions

**Can the agent just ask the user to click around?**

A wizard is better when the steps repeat or have safety-sensitive branches. It does not hide credentials or pretend to perform human-only actions.

## It's working if

- The wizard is explicit about secrets, validates inputs, supports cancellation, and leaves a reproducible handoff.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

a deployment, cloud, account, secret, or cutover step requires human authority or a visual third-party UI. It sits beside research for provider facts and pr for recording the resulting configuration change, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
