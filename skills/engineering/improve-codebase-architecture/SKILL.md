---
name: improve-codebase-architecture
description: Survey a codebase for high-leverage module deepening opportunities and turn one selected opportunity into an actionable change.
disable-model-invocation: true
---

# Improve Codebase Architecture

1. Map the target module, callers, callees, data ownership, and change history.
2. Look for shallow wrappers, pass-through APIs, duplicated policy, leaked representation, and seams that cannot be tested without internals.
3. Describe each candidate as current pain -> deeper boundary -> smallest safe migration.
4. Rank by user impact, change frequency, risk, and reversibility.
5. Select at most one candidate for the next cycle.
6. Write a small spec before editing code.

Do not optimize architecture in the abstract. A module earns redesign when real work is repeatedly paying for its current shape.
