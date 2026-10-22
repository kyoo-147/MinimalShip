# Worker task envelope

```text
TASK: one result
USER VALUE: the product outcome it serves
OWN: files, worktree, or branch
CONTRACT: interfaces with neighboring work
DO: must-have behavior
DO NOT: unrelated refactor, dependency, or deployment
CHECK: exact verification command
FINISH: changed paths, evidence, limitations, and commit if applicable
```

The lead owns shared contracts, manifests, and integration. A worker never edits a path another active worker owns.
