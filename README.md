# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

MinimalShip is a focused product-development skill bundle for AI coding agents. It helps a lead agent turn a real user problem into a small, runnable increment, supervise bounded work, verify the actual journey, and improve from evidence.

It is a workflow and a set of composable instructions. It is not a coding model, cloud platform, autonomous deployment service, issue-tracker backend, or guarantee of same-day completion.

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
2. one compact `RUN.md` record
3. one runnable vertical slice when the environment allows it
4. exact verification commands and factual PASS / FAIL / BLOCKED results
5. a SHIP, REVISE, or BLOCKED decision grounded in observed behavior

## Core loop

| Phase | Question | Proof of progress |
|---|---|---|
| READ REALITY | What exists and what can actually run? | Repository facts and available commands |
| ASK | Which decisions are still owned by the user? | One accepted outcome and permission contract |
| SPEC | What behavior is in and out? | `RUN.md` and acceptance cases |
| PLAN | What is the smallest dependency-aware slice? | Owned tasks with checks |
| DISPATCH | Which work is safe to parallelize? | Verified orchestrator, cap, and task envelopes |
| BUILD | Does the critical path work end to end? | Runnable increment |
| VERIFY | What did we actually execute? | Evidence and failure cases |
| SHIP | Can another person use and review it? | Branch, PR, merge, and post-merge verification when authorized |

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

The installer copies the root skill bundle only. It does not install Pi, Herdr, an orchestrator, dependencies, credentials, or cloud tooling.

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
├── references/                      # Root workflow guidance
├── templates/                       # RUN, spec, and ADR shapes
├── handbook/                        # Public human-facing skill pages
├── .agents/                         # Invocation, release, and authoring rules
├── .claude-plugin/                  # Plugin and marketplace manifests
└── scripts/                         # Install, link, list, sync, and check tools
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

## Maintainer checks

```bash
python scripts/check.py
bash scripts/list-skills.sh
node scripts/sync-plugin-version.mjs --check
```

Run the installer smoke test against a temporary project before changing the distribution boundary. Use `npm run check` when Node package metadata is available.

## Architecture reference

The repository shape was compared with [mattpocock/skills](https://github.com/mattpocock/skills) and the supplied MinimalShip v0.3 bundle. The comparison informed composability, invocation metadata, manifests, handbook pages, and validation. MinimalShip's instructions, examples, and product principles are independently written.
