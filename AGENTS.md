# MinimalShip Agent Rules

MinimalShip is a product-development skill bundle. **Build what matters. Ship what works. Improve what users need.**

## Product standard

Start from a real user problem, ship the smallest valuable solution, measure the outcome, and improve from evidence. Prefer simple, focused, maintainable solutions over speculative scope.

## Required delivery workflow

Treat every feature, fix, refactor, configuration change, skill, and release as production work:

1. Clarify the requirement, constraints, acceptance criteria, and risks.
2. Inspect the relevant code, tests, configuration, and history.
3. Create a focused branch from the current integration branch using `feat/`, `fix/`, `refactor/`, `chore/`, or `docs/` as appropriate.
4. Plan non-trivial work before editing.
5. Implement the smallest complete solution.
6. Add or update tests for changed behavior and important edge cases.
7. Run relevant tests, lint, formatting, type checks, builds, security checks, and smoke checks.
8. Review the complete diff for correctness, scope, regressions, secrets, and unnecessary changes.
9. Create a concise Conventional Commit.
10. Push the branch and open or update a pull request.
11. Wait for required CI and review; address failures and comments.
12. Merge only after required checks pass and review is complete.
13. Verify the merged result and relevant runtime behavior.
14. Report changed files, validation evidence, commit or PR references, and remaining risks.

Do not call work complete before verification. If a step is blocked, report the exact blocker and evidence.

## Bundle architecture

- `SKILL.md` is the root Pi workflow and keeps `/skill:minimalship` stable.
- `skills/engineering` and `skills/productivity` contain promoted composable skills.
- Every promoted skill has `SKILL.md`, `agents/openai.yaml`, a handbook page, bucket index entry, root README entry, and plugin manifest entry.
- `misc`, `in-progress`, and `deprecated` are structural buckets and are not promoted.
- `references/` and `templates/` belong to the root workflow.
- `handbook/` is the public documentation tree because `docs/` is local-only in this repository.
- `.agents/` contains authoring, invocation, release, and decision records.

## Invocation rules

User-invoked skills are explicit orchestration commands and must set `disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Model-invoked skills are reusable disciplines and omit both restrictions. Keep the two metadata surfaces synchronized.

Skills may point users to sibling skills, but operative dependencies must name the skill to call explicitly. Do not make one user-invoked skill silently invoke another.

## Local-only material

Never commit or push:

- `docs/`
- `analysis/`
- `.local/`
- credentials, `.env` files, private keys, or machine-specific configuration

Do not add copied source archives or byte-preservation indexes to the public package.

## Scope and safety

Read this file before modifying the repository. Preserve behavior outside the requested scope, prefer reversible changes and explicit validation, and do not delete data or close resources without confirming the target and impact. Normal implementation, Git, PR, CI, and merge permission does not authorize exposing secrets or bypassing safety checks.

## External effects

Pi and Herdr are optional runtime integrations. Choose one primary orchestrator when dispatching. Cloud dashboards, credentials, paid APIs, deployments, migrations, and destructive commands require explicit approval and truthful post-action verification.

## Git and GitHub

Do not push directly to `main` for normal work. Use focused branches, Conventional Commit subjects, authenticated GitHub tooling such as `gh`, and reviewable pull requests. Never force-push, rewrite shared history, bypass checks, or merge unreviewed work without an explicit exception.
