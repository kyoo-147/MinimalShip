---
name: tdd
description: Use a behavior-first red, green, refactor loop at agreed public seams.
---

# Test-Driven Development

1. Agree the seam and the behavior it protects.
2. Write one failing test with a concrete input and expected result.
3. Implement only enough code to make it pass.
4. Refactor names and structure without changing behavior.
5. Repeat for the next meaningful case.
6. Run the focused test, then the relevant suite and smoke path.

Avoid tests coupled to private methods, snapshots that restate implementation, and mocks that replace the behavior under test. See `tests.md` and `mocking.md` in this skill for the detailed patterns.
