# MinimalShip v0.5 major update - 2026-10-22

This is the active-cycle checkpoint for the research-grounded major update. The product inventory lives in `FEATURES.md`; this file records only current execution state, evidence and resume information.

## Current cycle

- Current project objective / Primary objective: add behavioral proof, opt-in stack-aware routing and repeatable runtime/resume evidence without growing MinimalShip into a framework.
- Branch / worktree: `feat/major-update-evals-routing` / repository root; code-changing workers use isolated worktrees
- Mode: release
- Current MUST scope (feature IDs): F7, F8, F9, F10
- Current NOT NOW scope: P2 context/memory/telemetry optimization, new promoted skills, vendored external repositories, cloud/EAS operations, release tag and merge bypass
- Exact next action: wait for PR #8 review and CI recovery; if billing/auth blockers clear, rerun Actions and the explicit evaluator before considering merge
- Last meaningful update: committed `fef70a2`, pushed `feat/major-update-evals-routing`, and opened stacked PR #8 against `feat/refine-workflow-state`

## Confirmed decisions

- User / problem: MinimalShip must prove agent behavior, select external specialist guidance only when evidence warrants it, and remain minimal, resumable and evidence-driven.
- Desired result and leading measure: a lead can take a project from READ through ITERATE with explicit feature inventory, approval, bounded ownership, real verification and honest blockers; leading measure is reproducible PASS/FAIL/BLOCKED evidence for E01-E08 and runtime boundaries.
- Constraints and assumptions: preserve the root skill and 27 promoted skills; keep public content original English; keep `docs/`, `analysis/` and `.local/` local-only; do not vendor third-party skill repositories; do not install, deploy or charge external services automatically.
- Decisions already settled: use one primary Herdr orchestrator with Pi as lead; maximum two workers; isolate code-changing workers; lead owns shared docs/manifests/integration; existing project versions/configuration remain authoritative; official Cloudflare, Expo and Vercel guidance is opt-in and project-scoped.
- Open decision or `BLOCKED` item: the explicit evaluator route is currently blocked by an invalidated OAuth token; the default configured `gpt-6.1-sol` path remains unsupported. Native/device, EAS, cloud and deployment checks remain unavailable unless separately approved; GitHub Actions is billing-blocked.

## Acceptance and demo

| ID | Real input/action | Expected result | Evidence command or observation | Status |
|---|---|---|---|---|
| A1 | Run the existing structural, installer, profile, link and workflow checks | Prior verified functionality remains green | `npm run check`, `bash scripts/list-skills.sh`, all smoke scripts and version check | PASS |
| A2 | Refresh global/profile installs and run the installed Pi loader | Root plus 27 promoted skills resolve with no loader diagnostics | `python scripts/smoke-runtime.py`: Pi loader PASS, global 29 / profile 28 observed | PASS |
| A3 | Run the E01-E08 behavioral evaluator with live adapter when available | Each scenario emits structured PASS, FAIL or BLOCKED; no blocked case is mislabeled PASS | `python scripts/run-evals.py --json --model openai-codex/gpt-5.6-luna --output .local/evals-v05-live.json`: all E01-E08 `BLOCKED` because the OAuth token was invalidated; exit 2 preserved | BLOCKED |
| A4 | Run deterministic evaluator/schema and baseline checks | Eight scenarios, expected outcomes and graders are complete and machine-readable | `python scripts/grade-evals.py --check` and `python scripts/route-stack.py --self-test` | PASS |
| A5 | Run stack-routing positive and negative fixtures | Only evidence-backed official external guidance routes; no auto-install/deploy/charge | `python scripts/route-stack.py --self-test`; source/version evidence in `references/stack-routing.md` | PASS |
| A6 | Run runtime, ownership, resume and release-boundary smoke checks | Pi/Herdr capability and unavailable states are explicit; overlap/false completion/resume rules hold | `python scripts/smoke-runtime.py`: structural/fixture, fresh-install loader, Pi and Herdr probes PASS; live worker dispatch is explicitly `BLOCKED` | BLOCKED |
| A7 | Run current official-source/version and documentation consistency checks | Routing source policy, QA gates, templates and indexes agree | `python scripts/check.py`, `python scripts/smoke-workflow.py`, authenticated official GitHub metadata refresh | PASS |
| A8 | Run full local gate and inspect complete diff | No unrelated changes; required checks are PASS or honest BLOCKED | Full local gate and diff review below; CI remains billing-blocked before steps | PASS |

## Approved execution policy

- Lead CLI / provider / model / thinking: Pi; explicit `openai-codex/gpt-5.6-luna` evaluator route is configured but blocked by invalidated OAuth; default `gpt-6.1-sol` selection is unsupported in this ChatGPT account
- Worker CLI / provider / model / thinking: Pi workers through Herdr; `openai-codex/gpt-5.6-luna`, low thinking for bounded implementation
- Reviewer model, if any: lead plus independent diff/evidence review; no additional paid reviewer
- Primary orchestrator: Herdr; Pi remains the lead and decision owner; no competing orchestrator
- Maximum workers / budget: two concurrent workers; bounded local task budget; no paid API, cloud or EAS spend
- Worktree and file ownership policy: worker A owns `evals/**` and eval scripts; worker B owns `references/stack-routing.md` and route detector; lead owns `SKILL.md`, state/docs, package/check/CI integration and all shared contracts
- Allowed edits, tools, installs, downloads, network, cloud and deployment: repository edits, local tests, read-only official-source verification, Git operations and existing authenticated runtime inspection; no new package install, cloud/EAS operation, deployment or destructive command
- Explicit approval still needed for: paid model/API use, external skill installation, cloud/EAS actions, credentials, deployment, destructive operations and release publication

## Tasks and ownership

| ID | Feature | One bounded result | Owner | Paths/worktree | Depends on | Size | Definition of done / check | Status |
|---|---|---|---|---|---|---|---|---|
| T5 | F7 | Add scenario schema, eight fixtures, deterministic grader and optional live Pi evaluator | lead (worker-a delivered) | integrated `evals/`, `scripts/run-evals.py`, `scripts/grade-evals.py` | F4, F5 | M | schema check passes; safe adapter emits honest JSON statuses and preserves BLOCKED | DONE |
| T6 | F8 | Add evidence-based official stack routing reference and deterministic detector | lead (worker-b delivered) | integrated `references/stack-routing.md`, `scripts/route-stack.py` | F1, F4 | M | positive/negative fixtures pass; no install/deploy commands; source commits recorded | DONE |
| T7 | F9 | Integrate repeatable runtime, ownership, resume and release-boundary checks | lead | repository root; `scripts/smoke-runtime.py`, state fixtures and integration docs | F7 | M | runtime report distinguishes PASS/FAIL/BLOCKED; resume/ownership fixtures pass | VERIFYING |
| T8 | F10 | Align READ-to-ITERATE core workflow, templates, docs, CI and version/changelog metadata | lead | shared root docs, templates, scripts, package/CI | T5, T6 | M | full local gate plus complete diff review | DONE |

## Active workers and dependencies

- Active workers: none; bounded worker-a/worker-b worktrees were reviewed and integrated, while user-controlled panes remain untouched
- Ready frontier: lead-owned final review, commit, push and PR creation; live evaluator, CI and native/cloud checks remain blocked
- Shared files or contracts with one owner: lead owns root workflow, `FEATURES.md`, `RUN.md`, templates, package metadata, CI, check script and integration decisions
- Worker reports awaiting integration: none; implementation outputs are integrated and lead-owned checks have been rerun

## Resume checkpoint

- Checkpoint ID: `v0.5-integrated-local-gate`
- Current branch: `feat/major-update-evals-routing`
- Last verified: structural, workflow, routing, eval-schema, compile, diff, Pi-loader, Herdr and deterministic runtime checks passed; live gaps remain BLOCKED
- Settled requirements: preserve 27 skills; add E01-E08 behavior evidence; opt-in official routing; no auto-install/deploy; two isolated workers; honest PASS/FAIL/BLOCKED
- Current blockers: native/device runtime unavailable for E08; default `gpt-6.1-sol` selection remains unsupported; GitHub billing lock and unavailable native/cloud services remain
- Exact next action after resume: inspect PR #8 review/CI status; do not merge while CI is billing-blocked or required review is absent
- Do not repeat: prior F1-F6 installer/profile/workflow implementation, source audit or worker implementation work

## Verification and evidence

- Run / build / start / smoke command: `npm run check`; `bash scripts/list-skills.sh`; `node scripts/sync-plugin-version.mjs --check`; all smoke scripts; `python scripts/route-stack.py --self-test`; `python scripts/grade-evals.py --check`; `python -m compileall -q scripts`; `git diff --check`
- Tests, typechecks, lint, format, build and security checks actually executed: structural, installer, link, profile, workflow, routing, eval-schema, compile and diff checks passed; Ruff/Pyright are unavailable; no product runtime build is required for this bundle
- Primary journey evidence: E01-E08 schema/fixtures and safe planning-only adapter are integrated; no-Pi probe returned BLOCKED for every scenario without mislabeling
- Important failure-case evidence: ownership overlap, false completion, resume checkpoint, install boundary and unavailable runtime states passed deterministic checks; live worker dispatch remains explicitly BLOCKED
- Latest results: E01-E08 `BLOCKED` on the latest live attempt; deterministic grader and runner self-tests `PASS`; F8/F10 `DONE`; F7/F9 `VERIFYING`; unavailable CI, native, cloud and deployment evidence remains `BLOCKED`, not PASS

## Blockers and next iteration

- Current blockers: explicit evaluator run fails authentication with `Encountered invalidated oauth token for user, failing request`; default Pi selection fails with `The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account`; GitHub Actions cannot start because the account is locked for billing; native/device, EAS, cloud, deployment and paid-service checks are unavailable or unauthorized
- Known limitations: no release tag or merged-result verification; live worker dispatch was not claimed by the non-mutating smoke command; research source commits remain provenance, not installation pins
- Measure or user feedback: deterministic checks now cover behavior schema, route precision, resume fidelity, ownership overlap, false completion and capability blockers
- Next highest-impact improvement: restore supported model/CI/native capabilities, rerun blocked checks, then address review or CI findings before merge or release
