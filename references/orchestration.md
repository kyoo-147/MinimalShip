# Herdr + Pi integration (2026-10-22 verified from project READMEs)

## A. Runtime and responsibilities
- **Pi**: host/Lead agent, model and coding tools.
- **Herdr**: pane/workspace runtime and agent process supervision, with Git worktree options.
- **Choose one default orchestration extension**:
  - `pi-herdsman` ([README](https://github.com/boadij/pi-herdsman)): ownership hierarchy Lead → Agent, optional Manager/Chief, nested delegation, project/branch assignment, session accounting. Strong fit for multi-worker orchestration. README install for pre-existing Pi+Herdr: `pi install npm:pi-herdsman`; `herdr integration install pi`; run `herdr`, `pi`. See `docs/getting-started.md`, `docs/guides/agent-definitions.md`, `docs/reference/agent-definition-schema.md`. User commands may change: use live installed version documentation. `/herdsman` and `/agents` in different docs/versions; do not assume one.
  - `pi-herdr` ([README](https://github.com/AndrewJacop/pi-herdr)): lightweight visible spawned agent panes; `herdr_spawn_agent`, `herdr_get_agent_result`, message/interrupt/resume/list and raw-pane controls; per-agent models, concurrency cap, queued starts, optional isolated worktrees; requirements per README: herdr ≥0.9.0, Node ≥20; install `pi install npm:@andrewjacop/pi-herdr`. Tested on Windows/macOS, Linux expected but unverified in cited README. Model settings are defined by extension; check actual installed tool/schema.
- **Do not install or activate both as the primary orchestrator.** If both present, disable one before the run and verify only one accepts dispatch.
- **Never invent an API surface**: check the installed extension's tool list and docs before delegated invocations.

## B. Model and worker gate — ask before spawning
Ask the user for Lead/implementer/reviewer agent CLI, model IDs, thinking levels, 'fast' preference, max workers, spending cap, and write/install/deploy permissions. Suggested answer format:
`Lead=pi/<model>, think=medium; Builders=pi/<model>, think=low, fast=on; Reviewer=<cli>/<model>, think=high; workers<=4; budget=...; worktrees=yes; install/deploy=<permissions>`
These are **examples**, not assumed defaults. 'fast' mode may not exist for a chosen CLI/model. Never assume high context or free credits. Use exact validated provider/model identifiers.

## C. Worktree strategy
1. Lead owns integration contracts and `RUN.md`.
2. Independent code writers: one branch/worktree and file ownership each; no shared mutable dependency manifests unless reserved to one worker.
3. Read-only scout/reviewer can inspect without worktree where safe.
4. Merge stable small slices serially with build/tests between merges; resolve conflicts explicitly.
5. If a unit cannot be isolated economically, use one worker; concurrency should be earned, not gamified.
6. Use Herdr agent/pane status and native completion receipts rather than guess from spinners or mere spawn success.

## D. Worker task envelope
```
TASK: <one result>
INPUT/USER VALUE: <goal>
OWN: <paths / worktree / branch>
CONTRACT: <interfaces with neighbors>
DO: <must-haves>
DO NOT: <unrelated refactor / dependencies / extra features>
CHECK: <one command + expected result>
FINISH: <paths changed, command/output, known issue, commit ID if created>
```

## E. Lavish AXI
- Lavish is **an HTML feedback/review editor**, **not** an agent orchestrator, backlog manager, or coding runtime.
- Primary source: https://github.com/kunchenguid/lavish-axi
- Install the public skill: `npx skills add kunchenguid/lavish-axi --skill lavish` (agent-specific discovery may vary); or invoke current CLI `npx -y lavish-axi --help` without a global install.
- For HTML artifact presentation, open with `npx -y lavish-axi path/to/plan.html`, annotate, and feed updates into `RUN.md`.
- Don't make it mandatory for text-only spec or prevent same-day shipping. Avoid global hooks unless requested.

## F. Matt Pocock inspiration
Source: https://github.com/mattpocock/skills
- Small, composable instructions rather than process ownership.
- One focused interview for genuinely missing requirements (`grill-with-docs` inspiration), not repeated exhaustive grilling.
- Shared vocabulary and explicit decision records **only if** naming/decision ambiguity is slowing work.
- Test behavioral seams and use small red→green steps for high-risk logic (`tdd` inspiration), not for appearance of thoroughness.
- Run product end-to-end and capture feedback; prioritize working behavior rather than documentation volume.

## G. Official Pi skill format
Docs: https://pi.dev/docs/latest/skills
- User install path: `~/.pi/agent/skills/minimalship/SKILL.md`; project path: `.pi/skills/minimalship/SKILL.md`.
- Invoke: `/skill:minimalship <goal>` (or skill discovery by description).
- Copy/installation only. It cannot spawn agents until running inside a configured Pi+Herdr session.
