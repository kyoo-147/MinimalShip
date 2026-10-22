# MinimalShip behavioral evaluations

`scenarios.json` defines the required E01-E08 behavior set from the v0.5 research brief. Each scenario has a prompt, fixture input, expected behavior, failure modes, required evidence, a baseline comparison, and runtime requirements.

## Two evidence layers

1. `python scripts/grade-evals.py --check` validates the scenario/fixture contract without a model.
2. `python scripts/grade-evals.py --self-test` proves the grader preserves `BLOCKED` and rejects false completion without a model.
3. `python scripts/run-evals.py --json` runs the same prompts through a planning-only Pi adapter from isolated fixture directories when a usable authenticated runtime is available, then grades the captured result. It never grants tools, dispatches workers, installs packages, deploys, uses credentials or calls paid services.

A runtime result is not inferred from documentation or filesystem checks. `PASS` requires the required evidence and truthful output; `FAIL` means the adapter ran but behavior or evidence was wrong; `BLOCKED` means the required runtime or capability was unavailable. BLOCKED is never converted into PASS. The live command exits 2 when any scenario is BLOCKED so release scripts cannot silently treat an incomplete run as green.

## Scenario map

- **E01:** new project, plan-only, zero code/worker/deployment side effects.
- **E02:** existing verified, inferred and proposed features remain distinct.
- **E03:** settled scope/model/policy is reused without repeated questions.
- **E04:** overlapping worker ownership is rejected or serialized.
- **E05:** a worker's DONE/PASS claim is rejected when its check fails.
- **E06:** a fresh session resumes objective, decisions, blockers and exact next action.
- **E07:** Cloudflare plus React routes to relevant official guidance without changing stack or deploying.
- **E08:** Expo/native QA requires loading/empty/error/content and device evidence; EAS remains approval-gated.

The report includes the scenario, command/output evidence, observed status, grader result, baseline comparison and blocker reason. Save a report outside the public bundle when it contains runtime output or private paths.
