# Writing for Agents

## What it does

Write skills and agent-facing documents that are discoverable, bounded, composable, and safe to follow. It is deliberately scoped to one decision or delivery seam rather than becoming a second project-management system.

## When to reach for it

- **Invocation:** Type `writing-for-agents` or let the agent reach for it when the task matches its trigger description.
- **Boundary:** Reach for it when the work needs creating or changing a SKILL.md, AGENTS.md, CLAUDE.md, handbook page, template, or agent instruction.

## Writing for Agents in practice

Use progressive disclosure: metadata, a concise workflow, then targeted references and scripts. Explain why a rule exists. State boundaries, outputs, failure behavior, and verification. Keep invocation metadata synchronized across harnesses.

## Common questions

**Should an agent document repeat the whole workflow?**

No. Keep the primary skill short and move detailed material into resources loaded only when needed.

## It's working if

- An agent can find the instruction, know when to use it, follow it without guessing, and verify the result.
- The resulting artifact is shorter or clearer than the input without hiding unresolved risk.
- The next person can verify the result from the recorded evidence.

## Where it fits

creating or changing a SKILL.md, AGENTS.md, CLAUDE.md, handbook page, template, or agent instruction. It sits beside codebase-design for information hiding and code-review for reviewing instruction changes, which cover adjacent concerns. Use [ask-minimalship](https://github.com/kyoo-147/MinimalShip/blob/main/skills/engineering/ask-minimalship/SKILL.md) when you are unsure which path to choose.
