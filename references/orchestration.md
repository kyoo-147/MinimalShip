# Pi, Herdr, and external execution

## Execution approval

Planning does not authorize code-changing workers. Dispatch only after an explicit implementation instruction or approval of the current `RUN.md` proposal. Before dispatch, confirm only unresolved worker, model, thinking, cap, budget, orchestrator, worktree and permission settings; reuse settled values.

## Roles

- **Pi** is the lead agent, model host, coding surface, and decision owner.
- **Herdr** is an optional visible pane and process runtime. It supervises workers but does not decide product acceptance.
- **An orchestrator** is an optional Pi extension. Select one primary integration, verify its installed tool names, and do not run competing dispatch surfaces together.
- **A worker** owns one bounded result, not the whole product.
- **A reviewer** supplies independent evidence and findings.

## Before dispatch

Check `pi --version`, the installed Herdr version and server status, the actual extension package, and the current branch. Confirm the user's worker/model/thinking/cap budget and permissions before spawning. If any of these are unknown, work locally or ask once.

## Worktree and ownership

The lead owns `RUN.md`, shared interfaces, schemas, manifests, and integration. Code-changing workers use separate worktrees or disjoint paths. Never let two active workers edit the same file. Integrate small slices serially and rerun affected checks after each integration.

## Task envelope

```text
TASK: one result
USER VALUE: the outcome it serves
OWN: files, worktree, branch
CONTRACT: interfaces with neighbors
DO: must-have behavior
DO NOT: unrelated refactor, dependency, or deploy
CHECK: exact command and expected result
FINISH: changed paths, evidence, limitations, commit if any
```

## Cloud and external effects

Cloud dashboards, credentials, paid APIs, deployments, migrations, and destructive commands are separate approval boundaries. The agent may prepare commands or a wizard, but it must not claim that a human-only action happened. Keep credentials out of `RUN.md`, logs, commits, and handoffs.

## Lavish and visual review

An HTML review tool may help inspect a complex plan or design. It is presentation and feedback, not orchestration, backlog storage, or a prerequisite for coding. Skip it when a text contract is clear.
