# MinimalShip Agent Rules

This file defines the default working agreement for every agent operating in this repository.

## Product standard

Build what matters. Ship what works. Improve what users need.

Start from a real user problem, ship the smallest valuable solution, measure the outcome, and improve from evidence. Prefer simple, focused, maintainable solutions over speculative scope.

## Required delivery workflow

Treat every feature, fix, refactor, configuration change, skill, and release as production work:

1. Clarify the requirement, constraints, acceptance criteria, and risks.
2. Inspect the relevant code, configuration, tests, and project history.
3. Create a focused branch from the current integration branch:
   - `feat/<short-name>` for features
   - `fix/<short-name>` for bug fixes
   - `refactor/<short-name>` for structural changes
   - `chore/<short-name>` for maintenance and tooling
   - `docs/<short-name>` for publishable repository documentation
4. Plan the change before editing when the work is non-trivial.
5. Implement the smallest complete solution.
6. Add or update tests for changed behavior and important edge cases.
7. Run the relevant validation before review: tests, lint, formatting, type checks, build, security checks, and manual smoke checks as applicable.
8. Review the complete diff for correctness, scope, regressions, secrets, and unnecessary changes.
9. Create a concise Conventional Commit.
10. Push the branch to the remote.
11. Open or update a pull request targeting `main`, including summary, testing evidence, risks, and follow-up work.
12. Wait for required CI checks and review feedback. Address failures and comments on the branch.
13. Merge only after required checks pass and review is complete.
14. Verify the merged result on `main` (tests/checks, status, and relevant runtime or deployment behavior).
15. Report what changed, what was verified, the commit/PR/merge references, and any remaining risks.

Do not call work complete before the required verification and delivery steps are complete. If a step is blocked, report the exact blocker and evidence rather than silently skipping it.

## Git and GitHub rules

- Do not push directly to `main` for normal work. Use a branch and pull request.
- Keep commits focused and use Conventional Commit subjects such as `feat(scope): add ...`, `fix(scope): prevent ...`, or `chore(scope): configure ...`.
- Never force-push, rewrite shared history, bypass required checks, or merge an unreviewed change unless the user explicitly requests that exception.
- Use authenticated GitHub tooling (prefer `gh`) for repository, issue, PR, and CI operations.
- Keep branches and pull requests small enough to review.

## Local-only working material

The following directories are private working space and must never be committed or pushed:

- `docs/` — local reference material and notes
- `analysis/` — local analysis and audit output
- `.local/` — machine-specific working files

Use these locations for temporary research and analysis. Keep secrets, credentials, `.env` files, and machine-specific configuration out of Git as well.

## Scope and safety

- Read this file before modifying the repository.
- Preserve existing behavior outside the requested scope.
- Prefer reversible changes and explicit validation.
- Do not delete data, close resources, or perform destructive operations without confirming the target and impact.
- Full operational permission means the agent may perform the normal implementation, Git, PR, CI, and merge steps required above; it does not authorize bypassing safety checks or exposing secrets.
