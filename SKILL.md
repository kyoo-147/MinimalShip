---
name: minimalship
description: MinimalShip is an English, product-development workflow for Pi Coding Agent and optional Herdr workers. Use when understanding a project, clarifying a focused increment, planning bounded work, coordinating approved agents, or verifying a delivery without overengineering.
disable-model-invocation: true
---

# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

MinimalShip is a compact product-development workflow, not a project-management framework, hosted task tracker, coding model, deployment service, or promise of autonomous completion. The lead agent protects the user's outcome, keeps one cycle focused, and reports evidence honestly.

## Operating rule

Run this sequence:

**READ → CLARIFY → FEATURES → SPEC → PLAN → APPROVE → DISPATCH → BUILD → VERIFY → SHIP → ITERATE**

Planning and execution are separate. A plan is not permission to edit product code or start workers.

## PROFILE GATE (OPTIONAL)

Read `references/profile.md` before applying operator-specific preferences.
A private profile is optional for ordinary project work:

- **No profile:** continue inspection, clarification, specification and local planning with neutral defaults. Report `PASS: PROFILE_OPTIONAL` and do not report `BLOCKED: PROFILE_INCOMPLETE` merely because no profile is configured.
- **Partial profile:** apply only explicit values and use neutral defaults for unresolved preferences. Ask only for a missing preference that affects the current decision.
- **Complete profile:** apply the completed modules without exposing their contents.
- **Execution boundary:** before worker dispatch or external/consequential effects, resolve the narrowest missing permission or orchestration decision. Use `python scripts/profile-status.py --require permissions` or `--require dispatch` when the helper is installed, or ask for a one-time explicit approval. Do not infer permission from silence.
- **Full profile:** use `--require profile` only when the user explicitly wants a completed personal profile. That strict check may report `BLOCKED: PROFILE_INCOMPLETE` and list profile questions.

Never infer private preferences from a name, previous session, recovery archive or unrelated repository. Never write private answers into the public bundle.

Read `references/orchestration.md` when workers, Herdr, worktrees or external effects are relevant. Read `references/grilling.md` when the user asks to grill or when high-risk ambiguity cannot be resolved safely in one round. Read `references/product-principles.md` when making a product-direction decision. Use the focused skills under `skills/` when a phase needs deeper discipline.

## Stack-aware external routing (optional)

During `READ`, inspect `references/stack-routing.md` only when local project evidence or the user's request suggests Cloudflare, Expo/EAS, React/Next/React Native or relevant UI work. Recommend the smallest official external skill family; do not vendor it, auto-install it, upgrade the existing toolchain, deploy, invoke paid EAS/cloud operations or use credentials. Existing dependencies, lockfiles and configuration remain authoritative. Record the route, source/version evidence, permission state and stack-specific QA in `RUN.md`. Missing browser, native/device or runtime capability is `BLOCKED`, never `PASS`.

## Behavioral evidence

Use `evals/scenarios.json` and `scripts/run-evals.py` for the E01-E08 behavior set when evaluating MinimalShip itself. Structural smoke tests prove contracts and files; they do not prove agent behavior. Live evaluation results must contain executed output and a deterministic grader result. A model/runtime limitation is `BLOCKED`, not a synthetic pass.

## Output contract

Every run aims to leave:

1. one concrete user outcome and a bounded MUST / NOT NOW scope;
2. a `FEATURES.md` inventory when the project needs feature tracking;
3. one compact `RUN.md` checkpoint for the current cycle;
4. one runnable vertical slice when the environment permits;
5. exact commands and factual `PASS`, `FAIL`, or `BLOCKED` results; and
6. a decision to `SHIP`, `REVISE`, or remain `BLOCKED` based on observed behavior.

`FEATURES.md` is the product inventory. `RUN.md` is the current execution record. Do not create `STATUS.md`, `TASKS.md`, `PLAN.md`, `BACKLOG.md` or another duplicate tracker by default.

## 1. READ (UNDERSTAND REALITY)

Read before asking:

- repository instructions, README files, specifications, tests, ADRs, glossary and recent decisions;
- source code and folder structure relevant to the request;
- existing functionality, incomplete functionality and unknown behavior;
- technology stack, package scripts, test/typecheck/lint/build/start commands and available runtime;
- the user's actual product goal and the smallest complete user journey.

For a new project brief, inspect the available project files first. For an existing repository, identify what already works before proposing changes. Separate:

- **FACT:** observed in the repository, tools or executed behavior;
- **DECISION:** owned by the user or explicitly approved;
- **ASSUMPTION:** reversible and clearly labelled; and
- **UNKNOWN:** must be answered or marked `BLOCKED`.

Do not repeatedly ask questions already answered in the repository, conversation, `FEATURES.md` or `RUN.md`.

## 2. CLARIFY

Ask one compact Quick round for only unresolved decisions:

- outcome, user, problem, deadline and example input/output;
- MUST, NICE, NOT NOW, platform, runtime and failure behavior;
- acceptance cases and leading measure;
- implementation authority when coding is requested, and risky-action permissions only when the current action needs them;
- worker or reviewer settings only if execution is authorized or dispatch is being considered.

Use Deep mode only when requested or when an unresolved branch could materially change behavior, architecture or safety. Give one practical recommendation for each question. Do not ask a long preference interview before ordinary development.

## 3. FEATURES

Create or update `FEATURES.md` before writing a spec when a project has more than a trivial change. Keep one row per feature and distinguish `EXISTING VERIFIED`, `REQUESTED`, `INFERRED` and incomplete work. Record user value, priority, complexity, acceptance criteria, dependencies and one owner. Use `TODO`, `READY`, `IN_PROGRESS`, `VERIFYING`, `DONE` or `BLOCKED`; `DONE` requires executed evidence for every acceptance criterion. Do not rebuild an existing verified capability from a claim alone.

## 4. SPEC

Create or update the smallest useful project state:

### `FEATURES.md` — product inventory

Use `templates/FEATURES.md` when feature tracking is needed. Keep one row per feature with:

- feature ID, name, user value and `EXISTING VERIFIED` or `REQUESTED` origin;
- priority `MUST`, `NICE` or `NOT NOW`;
- complexity `E`, `M` or `H`;
- status `TODO`, `READY`, `IN_PROGRESS`, `VERIFYING`, `DONE` or `BLOCKED`;
- dependencies, acceptance criteria and owner when assigned.

Existing verified functionality must remain distinguishable from newly requested work. A feature is `DONE` only after every required acceptance criterion has evidence. A failed, unexecuted or blocked criterion cannot be marked `DONE`.

### `RUN.md` — current execution record

Create or update the project-root `RUN.md` from `templates/RUN.md`. Keep it compact and current. It records the objective, confirmed decisions, current cycle MUST / NOT NOW scope, approved execution policy, task ownership, active workers and dependencies, latest verification results, blockers, exact next action and last meaningful update.

Do not duplicate the complete product inventory in `RUN.md`; link to feature IDs and record only the current cycle.

## 5. PLAN

Turn the acceptance cases into the smallest dependency-aware vertical slices:

- runnable skeleton or reproduction;
- primary input → action → result journey;
- critical must-haves and failure behavior;
- integration or migration only when needed;
- verification and delivery.

Every task has exactly one bounded result, one owner, allowed paths or an isolated worktree, dependencies, a size, a definition of done and exact checks. Shared contracts, schemas, manifests and integration files have one owner. If parallel execution provides no critical-path benefit, choose one agent.

At the end of planning, present a concise execution proposal. Do not start code-changing work or spawn workers merely because `FEATURES.md` and `RUN.md` are complete.

## 6. APPROVE

Proceed to execution only when one of these is true:

- the user explicitly authorized implementation in the request or a later message; or
- the user approved the presented proposal and its scope, policy and permissions.

Planning artifacts may be created or updated before approval. An implementation instruction authorizes only the stated scope; it does not silently authorize credentials, paid APIs, cloud dashboards, deployment, destructive commands or production data.

For prototype mode, require a runnable result, accepted scope, critical tests, demonstrable behavior and clear limitations. For release mode, also require review, regression and operational checks, required CI, approved merge and post-merge verification.

## 7. DISPATCH

Before starting code-changing workers, resolve only settings that are still unknown. Reuse settled values from conversation, `RUN.md` and an applicable profile. Confirm:

- lead coding agent;
- worker CLI/provider/model and supported thinking level;
- reviewer model when needed;
- fast/quality mode, if available;
- maximum concurrent workers and budget;
- one primary orchestrator, or none;
- worktree and file-ownership policy; and
- permissions for installs, network, external APIs, cloud operations and deployment.

Prefer Pi plus Herdr when available, but use one primary orchestrator rather than competing dispatch systems. Check the installed Pi and Herdr versions and actual integration surface before dispatch. If a setting is unsupported or unknown, do not invent it; ask once or work locally.

Each worker receives one task envelope with a task/feature ID, one result, relevant context, allowed paths or isolated worktree, contracts, dependencies, definition of done, exact verification commands, prohibited unrelated changes and an expected completion report. No two active code-changing workers own the same mutable file or shared contract. The lead owns `RUN.md`, shared interfaces, integration, evidence and final acceptance.

## 8. BUILD

Build the smallest complete vertical slice:

- input → processing → output;
- user action → API → persistence → confirmation; or
- upload → validation → processing → visible result.

Reuse the existing stack, libraries, infrastructure and conventions. Prefer boring, clear code. Use `tdd` when a behavior seam benefits from red → green → refactor. Avoid speculative abstractions, unrelated refactors, premature microservices and new infrastructure. A worker's pane, branch, commit or report is not product acceptance.

## 9. VERIFY

Verify the product journey, not merely the implementation:

- relevant tests, typecheck, lint, format, build and security checks;
- realistic input/output for the primary journey;
- an important failure scenario;
- end-to-end smoke behavior and relevant regressions; and
- UI, responsive, accessibility and state checks when a user interface is involved.

Record exact commands and observed results in `RUN.md`. Use only:

- `PASS: verified` when the check actually ran and passed;
- `FAIL: verification failed` when it ran and failed; or
- `BLOCKED: verification could not be completed` when the environment or permission prevented execution.

Update feature rows from evidence. Never mark a feature `DONE` from a plan, a green unit test alone, a worker completion message or an unexecuted command.

## 10. SHIP

Review the complete diff for correctness, scope, regressions, secrets and unnecessary changes. Use `code-review` and `pr` when the change warrants them. For release mode, use a focused branch and pull request, wait for required CI and review, merge only when approved, and verify the merged result. For a local prototype, deliver the runnable result and explicit limitations without pretending it is a production release.

If delivery is not authorized or a required check is unavailable, report the exact boundary rather than implying it happened.

## 11. ITERATE

After the cycle, compare the intended outcome with observed usage, feedback, failures, support cost and the leading measure. Keep, remove, revise or expand based on evidence. Update `FEATURES.md` and the next-action section of `RUN.md`; do not preserve a feature because it took effort to build.

## Non-negotiable boundaries

- Product evidence beats paperwork, feature count and agent count.
- One cycle has one primary objective and a bounded MUST scope.
- More documentation is not progress unless it changes a decision or makes verification easier.
- Cloud, deployment, credentials and external integrations are explicit risk boundaries.
- Never call an unexecuted check `PASS`.
- Never publish private profile contents or copied source material.

## Invocation map

- User-invoked orchestration: `ask-minimalship`, `grill-me`, `grill-with-docs`, `setup-minimalship`, `to-spec`, `to-tickets`, `implement`, `implement-spec`, `triage`, `wayfinder`, `improve-codebase-architecture`, `retro`, `handoff`, `to-questionnaire` and `teach`.
- Model-invoked discipline: `grilling`, `domain-modeling`, `codebase-design`, `prototype`, `research`, `tdd`, `code-review`, `pr`, `wizard`, `wait-what` and `writing-for-agents`.

Invoke a focused skill by name rather than loading the entire bundle into every turn.
