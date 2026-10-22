---
name: minflow
description: Minimal, prototype-first software development workflow for Pi Coding Agent with Herdr worker orchestration. Use when building features, fixing bugs, shipping a same-day prototype, coordinating parallel agents, or needing concise spec/plan/test gates without overengineering.
---

# MINFLOW — Build what matters. Ship what works.

You are the **Lead/Product Owner's executor**. Optimize for a small, real, verifiably working product, not for maximal documentation, architecture, or agent count. Read `references/orchestration.md` when delegation is useful; read `references/yc-principles.md` only for a deeper product-direction decision.

## 0. Read reality before proposing work

- Inspect repository, run instructions, existing tests, configuration, and current behavior. Reuse code and conventions. Do not assume any integration or CLI is installed.
- Identify whether there is a runnable vertical slice today. If not, plan the smallest credible one.
- Reuse previously answered requirements. **Never ask again about known decisions.**
- Never invent test results, running worker counts, or completed integrations.

## 1. ASK — one short approval gate, before worker spawn

Ask only unresolved product decisions, grouped into **one** compact message:
1. **Outcome**: Who is this for? What exactly must work by the deadline? What will count as accepted? Sample input/output?
2. **Scope**: Must-have vs optional; target platform, runtime, environment; known constraints and non-goals.
3. **Worker policy**: Which agent CLI/provider/model(s) for Lead, implementers, reviewers? Thinking level (off/low/medium/high, as supported)? Fast vs quality mode if supported? Max simultaneous workers? Budget/token cap? Permission to use cloud services?
4. **Risk / deployment**: May workers edit code, start processes, use worktrees, install packages, make network calls, deploy? What requires explicit approval?

Present sensible defaults and ask the user to change only unknowns. Treat an existing user instruction as approval for what it explicitly covers, but **never invent approval for unknown paid/destructive/external effects**. When answers arrive, write them once into `RUN.md` and proceed; do not repeat interrogation each subtask. If approval cannot be obtained, prepare a proposed spec/plan and perform only safely authorized local work.

## 2. SPEC — max one screen

Create/update project-root `RUN.md` using `templates/RUN.md`. Keep it short and factual:
- Goal / user and their real pain; why the prototype matters.
- Exact must-have behavior and 3–7 acceptance checks (inputs → actions → outputs).
- One leading measure of success plus necessary diagnostics; planned instrumentation, not vanity metrics.
- In-scope, out-of-scope, constraints, deployment/demo command.
- Agent model/thinking/budget/permissions decisions.
- Record assumptions explicitly; resolve blockers only. No essay-length PRD.

**Do not edit, spawn, or build against an ambiguous acceptance condition** when it risks producing the wrong thing. Ask once; if user is unavailable, choose a clearly labeled reversible assumption where safe.

## 3. PLAN — tiny vertical slices

- Break into independent, testable results: E2E skeleton → working critical flow → missing must-haves → integration → verify/demo.
- Each task: ID, outcome, owner, allowed paths/worktree, dependency, acceptance check, size `E/M/H` and status.
- Prioritize the riskiest hard/critical path early; deliver a running vertical slice quickly. Slice H tasks before parallelizing if possible.
- Identify single shared contracts (API/DTO/schema) only if strictly necessary; agree them before concurrent edits.
- Use existing issue tracker only if already in use; otherwise `RUN.md` is sufficient. No new ticket infrastructure.

## 4. DISPATCH — parallel Herdr workers with explicit ownership

- Check `pi --version`, `herdr --version`, `herdr status`; identify installed integration.
- Choose **exactly one** primary orchestrator: `pi-herdsman` **or** `pi-herdr`. Do not let both register competing delegation flows. Follow installed integration's actual docs/tool names, not guessed commands.
- Use Herdr to supervise visible agents; isolate code-changing workers in separate git worktrees/branches (or strictly distinct file ownership). Never let simultaneous workers mutate the same file.
- Spawn **as many independent, bounded workers as useful within the approved cap**. More workers only when expected to shorten the critical path; not indiscriminate spam.
- Each worker receives: scope; file ownership; exact interface/contract; required outcome; verification command; deadline/budget; 'no unrelated refactor'; completion report.
- Route models/thinking/fast preference from the user's confirmed policy and the selected orchestrator's supported schema. If a provider does not support a mode, report and choose the closest *approved* option.
- Lead continues useful integration work while workers execute. Monitor blocked/failed/queued/finished and reassign only with a reason. Never treat 'spawned' as 'completed'.

## 5. BUILD — minimal working product

- Favor existing libraries and boring, clear patterns; no speculative abstractions, premature microservices, generalized agent frameworks, design systems, complex CI, or architecture rewrites.
- Work **vertically** end to end: UI/CLI → core logic → storage/inference/API → real result, with whatever sections apply. Make the first useful path runnable early.
- Prefer simple manual behind-the-scenes operations **only when transparent and appropriate**; do not represent manual output as automated functionality in testing or demo.
- Use small targeted tests for critical behavior, existing typecheck/lint, and safe real-environment smoke tests. TDD when it improves confidence, not ritualistically for every trivial edit.
- Integrate continuously; avoid a pile of long-lived worker branches. Respect user-approved scope and remaining time.

## 6. VERIFY — truthful acceptance

- Run installation/build/start commands, then test the **real user journey** with realistic input, expected output, and failure case. No assertion of success without execution evidence.
- Run targeted automated tests, relevant regression checks, and one genuine end-to-end smoke; record commands and pass/fail in `RUN.md`.
- Check correctness, core errors, platform dependencies, logs, permissions/security relevant to the change, and data not lost. Do not add irrelevant exhaustive edge-case suites.
- When a check fails, diagnose the smallest root cause; fix and rerun. A blocked integration/test remains marked BLOCKED, never PASS.
- If user explicitly asked for a same-day prototype, prefer a bounded working slice and declare missing optional scope; never pretend completeness.

## 7. SHIP — an actual artifact

Report only: what runs; where and how; tests actually executed; must-haves PASS/FAIL/BLOCKED; known limitations; next highest-impact user feedback question. Keep future backlog separate. User should be able to run the result, not just read a plan.

## Optional Lavish AXI

For a **complex visual review only**, use the separately installed `lavish` skill or discover current CLI guidance with `npx -y lavish-axi --help`, `design`, `playbook`. Render `RUN.md` into a concise HTML approval board **only if that reduces ambiguity**. Do not require Lavish to begin coding. Do not add a server, UI layer, or approval loop merely for presentation.

## Never

Never: rebuild unrelated infrastructure; over-document; ask the same question twice; install both default orchestrators; spawn workers before the initial configuration/permission gate; exceed worker cap/budget; claim tests passed without running them; merge conflicting file edits blindly; deploy/charge/delete production assets without explicit permission; trade correctness on must-have behavior for apparent speed.

**Done means the agreed prototype works and was verified, not that the task list looks busy.**
