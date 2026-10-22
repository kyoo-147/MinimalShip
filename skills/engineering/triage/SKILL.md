---
name: triage
description: Move product and engineering reports through a small evidence-based state machine.
disable-model-invocation: true
---

# Triage

For each item:

1. Restate the observed user or engineering impact.
2. Separate report, reproduction, hypothesis, and proposed fix.
3. Check scope against `SCOPE.md` and existing decisions.
4. Reproduce or request the smallest missing evidence.
5. Assign a state, owner, next action, and acceptance signal.
6. Link a spec or ticket only when the item is ready for build work.

Do not turn every report into a feature. A well-supported decline is a useful product decision.
