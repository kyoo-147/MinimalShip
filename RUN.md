# MinimalShip refinement - 2026-10-22

This is the current-cycle checkpoint for the final workflow refinement. The product inventory lives in `FEATURES.md`.

## Current cycle

- Current project objective / Primary objective: make MinimalShip plan before execution, track state in two compact files, keep profiles optional, and harden installation evidence.
- Branch / worktree: `feat/refine-workflow-state` / repository root
- Mode: release
- Current MUST scope (feature IDs): F4, F5, F6
- Current NOT NOW scope: new skills, hosted tracking, new orchestration framework, release tag, CI billing remediation
- Exact next action: wait for required review/check resolution on PR #7; if billing is fixed, rerun Actions and verify the merged result
- Last meaningful update: pushed `feat/refine-workflow-state` and opened PR #7; local gate passed and live Actions failed before steps because of the account billing lock

## Confirmed decisions

- User / problem: MinimalShip must be clear, resumable and evidence-driven without forcing an unrelated profile interview or spawning workers before approval.
- Desired result and leading measure: a user can inspect a project, receive `FEATURES.md` and `RUN.md`, approve a bounded plan, then execute and verify one vertical slice; leading measure is successful local state/profile/installer smoke coverage.
- Constraints and assumptions: preserve the root skill and 27 promoted skills; keep public content neutral English; keep `docs/`, `analysis/` and `.local/` local-only; do not create duplicate trackers.
- Decisions already settled: use one primary orchestrator; require one owner per mutable file; distinguish planning from execution; use neutral defaults when no profile is configured; require scoped approval for workers and external effects.
- Open decision or `BLOCKED` item: GitHub Actions may remain blocked by the account billing lock; no release tag is claimed by this run.

## Acceptance and demo

| ID | Real input/action | Expected result | Evidence command or observation | Status |
|---|---|---|---|---|
| A1 | Run `python scripts/check.py` and `node scripts/sync-plugin-version.mjs --check` | Bundle structure and synchronized version pass | `PASS: MinimalShip bundle validated: 27 promoted skills, 5 references, 4 templates`; `PASS: plugin version 0.4.0` | PASS |
| A2 | Run profile, project and rollback installer smoke checks | Flat root plus 27 promoted skills install; conflicts and failed replacements are safe | `python scripts/smoke-install.py` -> PASS; `python scripts/smoke-links.sh` -> PASS | PASS |
| A3 | Run the profile smoke check with no profile, partial profile and scoped gates | Neutral defaults work; strict profile and execution boundaries remain explicit | `python scripts/smoke-profile.py` -> PASS; current private profile -> `PASS: PROFILE_COMPLETE`, `PASS: PERMISSIONS_READY`, `PASS: DISPATCH_READY` | PASS |
| A4 | Run the workflow contract smoke check | Ordered phases, state-file fields, approval gate, bounded tasks and evidence language are present | `python scripts/smoke-workflow.py` -> PASS | PASS |
| A5 | Inspect Pi and Herdr runtime | Pi and Herdr versions and active pane/runtime are known before dispatch | `pi --version` -> `1.4.0`; `herdr --version` -> `0.9.5`; server running and compatible; visible pane has no LSP/extension status widget | PASS |
| A6 | Run the installed Pi skill loader for global and separate-profile installs | Root and 27 promoted skills load without diagnostics; representative names resolve | Pi `loadSkills()` returned global 29 skills / profile 28 skills; `minimalship`, `implement`, `prototype`, `grill-me` all present | PASS |
| A7 | Inspect latest GitHub Actions run and annotations | Distinguish infrastructure/account failure from source failure | Run `39725819863` failed before steps; annotation says account locked due to billing issue | PASS |

## Approved execution policy

- Lead CLI / provider / model / thinking: current Pi session; use installed model settings; no unsupported model invented
- Worker CLI / provider / model / thinking: no worker required for this refinement; use Herdr only for an explicitly approved bounded task
- Reviewer model, if any: local structural and runtime checks; independent review if a PR requires it
- Primary orchestrator: none for implementation; Pi is lead and Herdr remains optional
- Maximum workers / budget: zero active workers for this branch unless separately approved
- Worktree and file ownership policy: lead owns all changed files; any future worker gets an isolated worktree or disjoint paths
- Allowed edits, tools, installs, downloads, network, cloud and deployment: repository edits, local tests, authenticated GitHub branch/PR operations and global/profile skill refresh; no deployment or production data
- Explicit approval still needed for: workers, credentials, paid APIs, cloud dashboards, migrations, deployment, destructive commands and release publication

## Tasks and ownership

| ID | Feature | One bounded result | Owner | Paths/worktree | Depends on | Size | Definition of done / check | Status |
|---|---|---|---|---|---|---|---|---|
| T1 | F4 | Add `FEATURES.md` and revise `RUN.md` plus root workflow for plan-before-execute | lead | `SKILL.md`, `README.md`, `templates/`, `FEATURES.md`, `RUN.md` | none | M | `python scripts/smoke-workflow.py` | DONE |
| T2 | F5 | Make private profile optional and gate only relevant permissions/orchestration boundaries | lead | `scripts/profile-status.py`, profile docs/templates/tests | F3 | M | `python scripts/smoke-profile.py` | DONE |
| T3 | F6 | Preserve unrelated installs and restore replaced paths after forced-install failure | lead | `scripts/install.py`, installer/link smoke tests, distribution docs | F2 | M | `python scripts/smoke-install.py` and `bash scripts/smoke-links.sh` | DONE |
| T4 | F4-F6 | Integrate checks, review diff, refresh installations and deliver branch | lead | repository-wide | T1-T3 | M | complete local gate and PR/CI evidence | VERIFYING |

## Active workers and dependencies

- Active workers: none
- Ready frontier: T4 local gate and delivery review
- Shared files or contracts with one owner: root workflow, state templates, installer and profile helper all owned by lead
- Worker reports awaiting integration: none

## Verification and evidence

- Run / build / start / smoke command: `npm run check`; `python scripts/smoke-install.py`; `bash scripts/smoke-links.sh`; `python scripts/smoke-profile.py`; `python scripts/smoke-workflow.py`
- Tests, typechecks, lint, format, build and security checks actually executed: full `npm run` check/smoke/version suite, Python compileall, shell syntax, `git diff --check`, pi-lens LSP diagnostics (5 files clean; one server inconclusive); Ruff/Pyright binaries are not installed in this shell
- Primary journey evidence: workflow contract confirms Understand → Clarify → Specify → Plan → Approve → Dispatch → Build → Verify → Ship → Improve and state records; installed Pi loader resolves root and representative commands
- Important failure-case evidence: incomplete profile uses neutral defaults; permission/dispatch gates block narrowly; forced installer failure restores previous paths; symlink target remains intact
- Latest results: `PASS` for all local checks above; PR #7 Actions run `39731313540` is `BLOCKED` by the account billing lock before job steps

## Blockers and next iteration

- Current blockers: GitHub Actions cannot start while the account billing lock remains; live post-merge CI evidence is unavailable
- Known limitations: a real model-backed `/skill:...` invocation could not complete because the available provider/model authentication did not accept the runtime selection; no worker was dispatched; no `0.4.0` release tag has been published
- Measure or user feedback: local contract and regression checks are green; runtime journey still needs a small bounded demonstration
- Next highest-impact improvement: complete the PR review, run a planning-only Pi journey if the provider is available, and resolve billing before relying on post-merge CI
