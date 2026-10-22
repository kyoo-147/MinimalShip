---
name: domain-modeling
description: Build a shared product vocabulary and keep code, acceptance, and decisions aligned with it.
---

# Domain Modeling

- Collect the nouns users and code already use.
- Ask what each term includes, excludes, and becomes in edge states.
- Identify commands, events, invariants, and ownership.
- Record stable definitions in `GLOSSARY.md`.
- Rename code only when the change reduces ambiguity and can be verified.
- Use ADRs for important boundary decisions, not for every naming choice.

The domain model is a compression tool. If it makes explanations longer, it is not ready.
