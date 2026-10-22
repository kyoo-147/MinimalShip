---
name: diagnosing-bugs
description: Use a disciplined reproduce, minimize, instrument, fix, and regression-test loop for hard bugs and performance regressions.
---

# Diagnosing Bugs

1. Capture the exact failure, environment, input, timing, and expected behavior.
2. Build a deterministic reproducer or record why one is currently blocked.
3. Minimize the input, call path, data set, or concurrency window.
4. Write competing hypotheses and identify the observation that separates them.
5. Instrument boundaries, not every line. Keep logs bounded and remove temporary noise.
6. Fix the violated invariant, then add a regression test at the public seam.
7. Run the original reproducer, root-cause variants, and relevant full checks.

If evidence remains ambiguous, report BLOCKED rather than calling a plausible patch a fix.
