---
name: implement-spec
description: Execute a complete spec as a dependency-aware task graph on one integration branch.
disable-model-invocation: true
---

Require an approved execution proposal or an explicit implementation instruction before dispatch. Planning completion alone is not permission to spawn workers.

# Implement Spec

- Validate the spec and task graph before spawning anything.
- Identify the ready frontier and reserve shared files to the lead or one owner.
- Give each worker a bounded task envelope: outcome, paths, contract, check, and finish report.
- Use isolated worktrees or disjoint file ownership for code changes.
- Integrate the smallest stable slice first, then rerun affected checks.
- Stop or replan when a worker discovers that the graph was wrong.
- Finish with end-to-end acceptance, a two-axis review, and a concise delivery report.

Never treat a spawned worker, green unit test, or merged branch as proof that the product outcome is complete.
