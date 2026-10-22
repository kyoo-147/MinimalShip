---
name: retro
description: Review a completed coding session and propose the smallest environment improvement with evidence.
disable-model-invocation: true
---

# Retro

- Review the request, decisions, tool calls, failures, corrections, and final evidence.
- Find repeated work, missing checks, unclear terms, and unsafe defaults.
- Classify each finding as product, codebase, tooling, instruction, or environment.
- Rank by recurrence x cost x ease of prevention.
- Propose the smallest test, script, rule, or doc change that would prevent it.
- Do not modify the environment silently; ask before installing or changing global behavior.

A retro is complete when the next session has a measurable chance of being easier or safer.
