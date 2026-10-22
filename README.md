# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

MinimalShip is a focused product-development skill bundle for AI coding agents. It helps a lead agent turn a real user problem into a small, runnable increment, supervise bounded work, verify the actual journey, and improve from evidence.

It is a workflow and a set of composable instructions. It is not a coding model, cloud platform, autonomous deployment service, issue-tracker backend, or guarantee of same-day completion.

## Current release
MinimalShip is currently released as **[v0.5.0](https://github.com/kyoo-147/MinimalShip/releases/tag/v0.5.0)**.
The release is the merged `main` state and includes the workflow, installer, profile, evaluation and routing updates described below.

### What is implemented now

The current bundle includes 27 promoted skills plus the root `/skill:minimalship` workflow, all discoverable as flat Pi siblings after installation.
It provides the READ → CLARIFY → FEATURES → SPEC → PLAN → APPROVE → DISPATCH → BUILD → VERIFY → SHIP → ITERATE loop with resumable `FEATURES.md` and `RUN.md` checkpoints.
It provides safe global, project and profile installation with conflict checks, atomic replacement and rollback coverage.
It keeps private profiles optional, uses neutral defaults for ordinary planning, and applies scoped permission and dispatch gates to consequential work.
It includes E01–E08 behavioral evaluation fixtures, deterministic grading, adversarial grader self-tests and runtime reporting.
It provides opt-in routing for relevant official Cloudflare, Expo/EAS and Vercel guidance without auto-installing, upgrading, deploying or charging.
It documents evidence-first review, verification, pull requests, merges and post-merge checks.

### Current verification state
The deterministic bundle, installer, profile, workflow and evaluation checks pass locally.
The live evaluation adapter and real worker dispatch remain conditional on an authenticated, supported runtime; unavailable capabilities are reported as `BLOCKED`, never presented as `PASS`.
GitHub Actions is currently blocked before workflow steps by the repository account billing lock. This is an infrastructure limitation, not a reported source-test failure.

## What it protects against

- building a large solution before validating a narrow need
- long PRDs that never become a runnable path
- workers editing the same files without ownership
- tests that prove implementation details instead of behavior
- hidden manual work presented as automation
- cloud, credential, or deployment effects that were never approved
- declaring success from a plan, a spinner, or an unexecuted check

## The output contract

A MinimalShip cycle aims to leave:

1. one user outcome and a clear MUST / NOT NOW boundary
2. one `FEATURES.md` inventory when feature tracking is needed
3. one compact `RUN.md` record for the current cycle
4. one runnable vertical slice when the environment allows it
5. exact verification commands and factual PASS / FAIL / BLOCKED results
6. a SHIP, REVISE, or BLOCKED decision grounded in observed behavior

## Core loop

| Phase | Question | Proof of progress |
|---|---|---|
| READ | What exists and what can actually run? | Repository facts and available commands |
| CLARIFY | Which decisions are still owned by the user? | One accepted outcome and permission contract |
| FEATURES | What already exists, is requested or is incomplete? | Evidence-backed feature inventory |
| SPEC | What behavior is in and out? | `FEATURES.md`, `RUN.md` and acceptance cases |
| PLAN | What is the smallest dependency-aware slice? | Owned tasks with checks |
| APPROVE | Is execution authorized for this scope? | Explicit approval or implementation instruction |
| DISPATCH | Which work is safe to parallelize? | Verified orchestrator, cap, and task envelopes |
| BUILD | Does the critical path work end to end? | Runnable increment |
| VERIFY | What did we actually execute? | Evidence and failure cases |
| SHIP | Can another person use and review it? | Branch, PR, merge, and post-merge verification when authorized |
| ITERATE | What did observed use teach us? | A measured next product decision |

Quick clarification is the default. Deep grilling is available when ambiguity could change product behavior, architecture, or safety.

## Install the root Pi skill

From a checkout of this repository:

```powershell
py .\scripts\install.py --global
```

Or install into a project:

```powershell
py .\scripts\install.py --project D:\work\my-project
```

Then run Pi with:

```text
/skill:minimalship Build a working prototype of <goal> and verify the primary user journey.
```

## Separate private profile

MinimalShip keeps the public bundle neutral.
Personal voice, opinions, UI taste, research habits, orchestration policy and permissions live in a separate profile directory.

```powershell
py .\scripts\init-profile.py --agent-dir "$env:USERPROFILE\.pi\profiles\minimalship"
py .\scripts\install.py --profile "$env:USERPROFILE\.pi\profiles\minimalship" --force
$env:PI_CODING_AGENT_DIR = "$env:USERPROFILE\.pi\profiles\minimalship"
$env:MINIMALSHIP_PROFILE_DIR = "$env:USERPROFILE\.pi\profiles\minimalship\profile"
py .\scripts\profile-status.py
pi
```

A missing or partial profile does not block ordinary project inspection or planning; the normal status is `PASS: PROFILE_OPTIONAL` or `PASS: PROFILE_PARTIAL` with neutral defaults.
Use `py .\scripts\profile-status.py --require permissions` or `--require dispatch` only when the current action needs that execution boundary. Use `--require profile` when the user explicitly wants a completed private profile; it can then report `BLOCKED: PROFILE_INCOMPLETE` and list the questions in `templates/profile/PROFILE-QUESTIONS.md`.
Answer with a concrete value, `not applicable`, or `use neutral defaults`.
Never commit the completed private profile to the public repository.

The installer installs the root bundle at `minimalship/` and each of the 27 promoted skills as a sibling directory so Pi can discover `/skill:minimalship` and `/skill:<promoted-name>` independently. It does not install Pi, Herdr, an orchestrator, dependencies, credentials, or cloud tooling.

## Bundle architecture

The repository follows a composable skill-bundle shape inspired by public Agent Skills repositories, while keeping all MinimalShip content original:

```text
MinimalShip/
├── SKILL.md                         # Root Pi workflow
├── agents/openai.yaml               # Root Codex metadata
├── skills/
│   ├── engineering/                 # Product engineering skills
│   ├── productivity/                # Product-workflow skills
│   ├── misc/                        # Optional, not promoted
│   ├── in-progress/                 # Experimental, not promoted
│   └── deprecated/                  # Retired, not promoted
├── references/                      # Root workflow, profile and stack-routing guidance
├── evals/                            # E01-E08 behavioral scenarios and fixtures
├── templates/                       # FEATURES, RUN, spec, ADR, and private-profile shapes
│   └── profile/                     # Neutral templates and first-run questions
├── handbook/                        # Public human-facing skill pages
├── .agents/                         # Invocation, release, and authoring rules
├── .claude-plugin/                  # Plugin and marketplace manifests
└── scripts/                         # Install, routing, eval, runtime, and check tools
```

This repository keeps `docs/`, `analysis/`, and `.local/` local-only by project policy. Public human-facing pages live under `handbook/` instead of the ignored `docs/` directory.

## Promoted skill map

### Engineering, user-invoked

- [ask-minimalship](skills/engineering/ask-minimalship/SKILL.md): choose the smallest flow
- [grill-with-docs](skills/engineering/grill-with-docs/SKILL.md): resolve consequential ambiguity with durable vocabulary
- [setup-minimalship](skills/engineering/setup-minimalship/SKILL.md): configure a repository once
- [to-spec](skills/engineering/to-spec/SKILL.md): compress a settled conversation into a spec
- [to-tickets](skills/engineering/to-tickets/SKILL.md): create dependency-aware slices
- [implement](skills/engineering/implement/SKILL.md): build one accepted slice
- [implement-spec](skills/engineering/implement-spec/SKILL.md): execute a full task graph
- [improve-codebase-architecture](skills/engineering/improve-codebase-architecture/SKILL.md): survey high-leverage module improvements
- [triage](skills/engineering/triage/SKILL.md): classify and move reports with evidence
- [wayfinder](skills/engineering/wayfinder/SKILL.md): resolve multi-session decisions
- [retro](skills/engineering/retro/SKILL.md): improve the environment from session evidence

### Engineering, model-invoked

- [codebase-design](skills/engineering/codebase-design/SKILL.md): design deep modules and seams
- [diagnosing-bugs](skills/engineering/diagnosing-bugs/SKILL.md): reproduce, minimize, instrument, fix, regress
- [domain-modeling](skills/engineering/domain-modeling/SKILL.md): align vocabulary and boundaries
- [prototype](skills/engineering/prototype/SKILL.md): answer one question with a disposable artifact
- [research](skills/engineering/research/SKILL.md): gather high-trust evidence
- [tdd](skills/engineering/tdd/SKILL.md): protect behavior with red, green, refactor
- [code-review](skills/engineering/code-review/SKILL.md): review standards and product spec separately
- [pr](skills/engineering/pr/SKILL.md): write an evidence-first pull request
- [wizard](skills/engineering/wizard/SKILL.md): guide human-only cloud and deployment steps

### Productivity, user-invoked

- [grill-me](skills/productivity/grill-me/SKILL.md): interview the user through consequential decisions
- [handoff](skills/productivity/handoff/SKILL.md): transfer a session without transcript noise
- [to-questionnaire](skills/productivity/to-questionnaire/SKILL.md): ask an unavailable decision owner asynchronously
- [teach](skills/productivity/teach/SKILL.md): build durable understanding through practice

### Productivity, model-invoked

- [grilling](skills/productivity/grilling/SKILL.md): run a dependency-ordered decision frontier
- [wait-what](skills/productivity/wait-what/SKILL.md): repair a misunderstanding before more work
- [writing-for-agents](skills/productivity/writing-for-agents/SKILL.md): author safe, composable agent instructions

## Product boundaries

MinimalShip keeps product development in scope: discovery, specification, prototyping, implementation, debugging, testing, review, release preparation, and bounded orchestration. It does not prescribe fundraising, founder identity, family decisions, age, investment outcomes, or startup theater. It does not copy or redistribute third-party source archives.

## Project state

When a project needs explicit feature tracking, `FEATURES.md` is the product inventory: it distinguishes existing verified behavior from requested work and owns feature priority, status and acceptance criteria. `RUN.md` is the current-cycle checkpoint: it owns the objective, decisions, approved execution policy, task ownership, active workers, evidence, blockers and exact next action. The root workflow does not create a separate status or backlog file by default.

MinimalShip plans before execution. It may create or update these two state files while researching, then presents the execution proposal. Code-changing work and worker dispatch begin only after explicit approval or an implementation instruction.

When a project shows Cloudflare, Expo/EAS, React, Next.js or React Native evidence, MinimalShip may recommend the smallest relevant official external skill family. Routing is opt-in and project-scoped: it never vendors, auto-installs, upgrades the stack, deploys or invokes paid services. See `references/stack-routing.md`.

## Maintainer checks

```bash
python scripts/check.py
bash scripts/list-skills.sh
node scripts/sync-plugin-version.mjs --check
python scripts/smoke-install.py
python scripts/smoke-links.sh
python scripts/smoke-profile.py
python scripts/smoke-workflow.py
python scripts/route-stack.py --self-test
python scripts/grade-evals.py --check
python scripts/grade-evals.py --self-test
python scripts/smoke-runtime.py
python scripts/init-profile.py --help
python scripts/profile-status.py --help
```

Run `python scripts/smoke-install.py` against a temporary profile before changing the distribution boundary. Use `bash scripts/link-skills.sh --check <target>` to inspect link conflicts, and pass `--force` only when replacement is deliberate. Use `npm run check` when Node package metadata is available. `smoke-runtime.py` is report-only: an unavailable live worker, device or model capability remains `BLOCKED`, never `PASS`. Run `python scripts/run-evals.py --json` only when the configured model-backed evaluation is authorized; its exit code is 2 when any scenario is blocked.

## Architecture reference

The repository shape was compared with [mattpocock/skills](https://github.com/mattpocock/skills) and the supplied MinimalShip v0.3 bundle. The comparison informed composability, invocation metadata, manifests, handbook pages, and validation. MinimalShip's instructions, examples, and product principles are independently written.
