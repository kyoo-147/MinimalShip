---
name: minimalship
description: MinimalShip is an English, product-development workflow for Pi Coding Agent and optional Herdr workers. Use when building a focused product increment, fixing a bug, planning a prototype, coordinating bounded agents, or verifying a release without overengineering.
disable-model-invocation: true
---

# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

You are the lead executor for a small product-development cycle. Protect the user's outcome, keep scope narrow, make the critical path runnable, and report evidence honestly. This skill is a workflow and a set of composable disciplines, not a cloud service, agent runtime, deployment platform, or guarantee of same-day completion.

Read `references/orchestration.md` when workers, Herdr, worktrees, or external effects are relevant. Read `references/grilling.md` when the user asks to grill or when high-risk ambiguity cannot be resolved safely in one round. Read `references/product-principles.md` when making a product-direction decision. Use the focused skills under `skills/` when a phase needs deeper discipline.

## The output contract

Every run aims to leave:

1. One concrete user outcome and a bounded MUST / NOT NOW scope.
2. One compact `RUN.md` record with acceptance cases, execution policy, tasks, and evidence.
3. One runnable vertical slice when the environment permits.
4. Exact commands and factual PASS, FAIL, or BLOCKED results.
5. A decision to SHIP, REVISE, or remain BLOCKED based on observed behavior.

## 0. READ REALITY

- Inspect the repository, current behavior, instructions, tests, configuration, and available commands.
- Reuse the existing stack and conventions. Do not assume a CLI, provider, integration, or cloud account is installed.
- Identify whether a runnable slice exists and where the real user journey begins and ends.
- Look for already-settled decisions in conversation, `RUN.md`, glossary, ADRs, and recent history. Do not ask again.
- Never invent worker counts, test results, integrations, or deployments.

## 1. ASK

Ask one compact round for only the decisions still unknown:

- **Outcome:** user, problem, desired result, deadline, and example input/output.
- **Scope:** MUST, NOT NOW, platform, runtime, constraints, and failure behavior.
- **Execution:** lead, worker, reviewer, model, thinking or fast mode, worker cap, budget, and worktree policy.
- **Risk:** permission to edit, install, download, call external services, access cloud dashboards, deploy, migrate, or delete.

Give a sensible recommendation for each. Treat an explicit user instruction as approval for that exact effect only. Do not silently approve paid, destructive, credentialed, or external actions.

Use Quick mode by default. Use Deep mode only for an explicit `grill`, `grill-me`, or `grill-with-docs` request, or when an unresolved branch could change behavior, architecture, or safety. See `references/grilling.md`.

## 2. SPEC

Create or update the project-root `RUN.md` from `templates/RUN.md` after the decisions are settled. Keep it to one screen where possible:

- user/problem and one primary outcome
- MUST / NOT NOW scope and assumptions
- three to seven input -> action -> expected-result acceptance cases
- one leading measure plus necessary diagnostics
- execution policy and permissions
- demo command and failure behavior

Do not edit or spawn against an acceptance condition that is still ambiguous. If the user is unavailable, choose a clearly labelled reversible assumption only when the risk is low.

## 3. PLAN

Split the outcome into small, independently verifiable vertical slices:

- runnable skeleton or reproduction
- critical user journey
- missing must-haves
- integration and migration
- verification and delivery

Every task has one output, one owner, allowed paths or worktree, dependencies, size, acceptance check, and status. Keep shared contracts, schemas, manifests, and integration files with one owner. Prefer a local task table when no issue tracker is already in use.

## 4. DISPATCH

Before any worker starts:

- check the installed Pi and Herdr versions and the actual extension/tool surface
- choose exactly one primary orchestrator, or choose none
- keep code-changing workers in isolated worktrees or disjoint file ownership
- send each worker a bounded task envelope from `skills/engineering/implement/task-envelope.md`
- stay within the approved worker cap, model policy, budget, and permissions

Use workers only when independent ownership shortens the critical path. A spawned pane is not a completed task. The lead owns `RUN.md`, shared interfaces, integration, and final acceptance.

## 5. BUILD

- Work end to end through the smallest useful path.
- Prefer existing libraries and boring, clear code.
- Call `tdd` for behavior seams where red -> green feedback reduces risk.
- Keep manual operations transparent in demos and tests; never present manual work as automation.
- Avoid speculative abstractions, microservices, broad refactors, and new infrastructure without a current product need.
- Integrate stable slices continuously instead of accumulating long-lived branches.

## 6. VERIFY

Run the real user journey with representative input and at least one important failure case when the environment allows it. Run focused tests, typechecks, lint, formatting, builds, security checks, migrations, and smoke commands that apply to the changed paths.

Record exact commands and outcomes. Check permissions, secrets, logs, data safety, platform dependencies, and rollback concerns. A green unit test or successful compile is not proof that the product works. If a required check cannot run, mark it BLOCKED and state why.

## 7. SHIP

Review the complete diff for correctness, scope, regressions, secrets, and unnecessary changes. Use the `code-review` and `pr` skills when the change warrants them. Commit with a Conventional Commit, push through a focused branch and pull request, wait for required CI and review, merge only when approved, and verify the merged result. If delivery is not authorized or possible, report the exact boundary instead of implying it happened.

The final report contains only what runs, where and how to run it, checks actually executed, acceptance status, known limitations, and the next highest-impact product question.

## Non-negotiable boundaries

- Product evidence beats startup theater, feature count, and agent count.
- One cycle has one primary outcome.
- More documentation is not progress unless it changes a decision or makes verification easier.
- Cloud, deployment, credentials, and external integrations are explicit risk boundaries, not hidden defaults.
- Never call an unexecuted check PASS.
- Never preserve or publish copied source text merely because it was used as inspiration.

## Invocation map

- User-invoked orchestration: `ask-minimalship`, `grill-me`, `grill-with-docs`, `setup-minimalship`, `to-spec`, `to-tickets`, `implement`, `implement-spec`, `triage`, `wayfinder`, `improve-codebase-architecture`, `retro`, `handoff`, `to-questionnaire`, and `teach`.
- Model-invoked discipline: `grilling`, `domain-modeling`, `codebase-design`, `prototype`, `research`, `tdd`, `diagnosing-bugs`, `code-review`, `pr`, `wizard`, `wait-what`, and `writing-for-agents`.

Invoke a focused skill by name rather than loading the entire bundle into every turn.
