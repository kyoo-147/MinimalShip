---
name: code-review
description: Review a diff on standards and product-spec axes, with separate evidence for correctness, scope, and design risk.
---

# Code Review

1. Pin the comparison point and verify the diff is non-empty.
2. Identify the originating spec or state that none exists.
3. Review the implementation against acceptance and scope.
4. Review design against repository rules, public seams, error handling, security, and unnecessary complexity.
5. Check changed behavior, callers, tests, generated files, secrets, and documentation.
6. Report findings with severity, path, evidence, and a minimal fix.
7. Re-run focused checks after fixes and keep the two axes separate.

A review that finds nothing should still state what it examined and what evidence was available.
