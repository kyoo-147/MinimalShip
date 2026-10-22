---
name: grill-with-docs
description: Resolve consequential product and architecture ambiguity while maintaining the project's vocabulary and decision records.
disable-model-invocation: true
---

# Grill With Docs

Use a deep interview when a product or architecture decision has branches that cannot be safely guessed.

1. Read the repository, existing glossary, ADRs, and current behavior before asking.
2. Build a private decision tree from outcome to user journey, constraints, acceptance, and risk.
3. Ask only the answerable frontier in compact numbered rounds, with a recommendation.
4. Separate facts discovered from decisions owned by the user.
5. After each round, update the shared contract and discard settled questions.
6. Write terms to `GLOSSARY.md` only when they change how the code should be named or understood.
7. Create an ADR only for a consequential, hard-to-reverse choice.

Finish with one acceptance contract. Do not start implementation while a high-risk branch is still silently assumed.
