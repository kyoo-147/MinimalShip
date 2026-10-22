---
name: codebase-design
description: Design deep modules and testable seams by hiding complexity behind small, honest interfaces.
---

# Codebase Design

When a change feels scattered:

1. Name the policy or invariant that should have one owner.
2. List the callers and the representation details they currently know.
3. Find the narrowest boundary that can own the policy without becoming a god module.
4. Move behavior toward that boundary, not data outward to every caller.
5. Keep adapters at the edge and domain decisions inside.
6. Test through the seam and compare the before/after caller burden.

Prefer a deep module with a small interface over a collection of shallow pass-through wrappers. Do not add generality without a current caller.
