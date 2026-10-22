# Set Up MinimalShip

## What it does

Configure a repository for the MinimalShip product-development workflow without imposing an issue tracker or hosted service. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** You invoke `setup-minimalship` explicitly, and the agent will not reach for it on its own.
- **Boundary:** Reach for it when the work needs first use of the bundle in a repository or a deliberate change to its working agreement.

## Set Up MinimalShip in practice

Setup is a one-time agreement, not a ceremony repeated for every feature. It identifies the source of truth for work records, the issue tracker if one already exists, local-only paths, test commands, and the selected Pi and Herdr integration.

## Common questions

**Does setup install a cloud backend?**

No. It configures local conventions and records optional integrations; it never creates accounts or deploys services.

## It's working if

- The repository has a clear owner, vocabulary, local work record, and verified tool boundaries.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

first use of the bundle in a repository or a deliberate change to its working agreement. It sits beside to-spec for the first feature contract and setup validation in the root scripts, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
