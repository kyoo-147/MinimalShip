---
name: writing-for-agents
description: Write skills and agent-facing documents that are discoverable, bounded, composable, and safe to follow.
---

# Writing for Agents

- Put trigger conditions in frontmatter descriptions.
- Keep `SKILL.md` focused and under a practical context budget.
- Use imperative steps, but explain the reason behind important constraints.
- Separate user-invoked orchestration from model-invoked reusable discipline.
- Prefer explicit skill calls over brittle relative-file dependencies between skills.
- Give every generated artifact a path, schema, and verification rule.
- Never include secrets, copied third-party text, or surprising side effects.

After editing a skill, validate its metadata, links, examples, and behavior against a few realistic prompts.
