# MinimalShip bundle rewrite - 2026-10-22

## Outcome
- User/problem: The previous package mixed a single Pi workflow with copied source archives, Vietnamese public pages, and limited composability.
- Deadline and deliverable: Rewrite the current branch as an original English product-development skill bundle with stable `/skill:minimalship` installation.
- One primary outcome: A clean checkout installs and validates a coherent root workflow plus focused engineering and productivity skills.
- One leading measure: A fresh project install exposes the root workflow and promoted skills without local-only or removed source material.

## Scope
- MUST:
  - Keep product-first workflow, Quick/Deep grilling, output contract, anti-overengineering policy, Pi/Herdr boundary guidance, and truthful PASS/FAIL/BLOCKED reporting.
  - Add composable skills, metadata, handbook pages, indexes, plugin manifests, governance, templates, and validation scripts.
  - Publish original English product-development content only.
  - Keep `docs/`, `analysis/`, and `.local/` local-only.
  - Remove copied source archives, hashes, line indexes, Vietnamese public README content, and unrelated startup material.
- NOT NOW:
  - A hosted service, issue-tracker backend, autonomous deployment platform, or new agent runtime.
  - History rewriting or publishing a release from this branch.
- Constraints and assumptions:
  - The root `/skill:minimalship` entry point remains stable.
  - Pi and Herdr are optional adapters; no vendor-specific orchestrator is required.

## Acceptance / demo
| ID | Real input/action | Expected result | Evidence | Status |
|---|---|---|---|---|
| A1 | Run `python scripts/check.py` | Structural, metadata, manifest, handbook, and removal checks pass | `PASS: MinimalShip bundle validated: 27 promoted skills, 4 references, 3 templates` | PASS |
| A2 | Install into a temporary project and global Pi skill path | Root workflow, references, templates, and promoted skills install without `.git`, local-only paths, project run record, or removed sources | Project and global installer smoke tests; global installed check passes | PASS |
| A3 | Inspect user-invoked and model-invoked skill metadata | Frontmatter and `agents/openai.yaml` agree on invocation policy | `scripts/check.py` validates all 27 skills | PASS |
| A4 | Read README, SCOPE, GLOSSARY, references, and handbook indexes | Product-development scope, terminology, orchestration boundaries, and package use are clear | Manual review and links in current tree | PASS |
| A5 | Run the package version synchronization check | Plugin version matches package version | `PASS: plugin version 0.4.0` | PASS |
| A6 | Run Pi version and inspect installed skill | Pi is available and global installation exposes `/skill:minimalship` content | `pi --version` -> `1.4.0`; installed SKILL.md present | PASS |

## Execution policy
- Lead: current Pi session; local implementation only.
- Workers: read-only architecture and reference inspections were used before implementation.
- Reviewer: local structural checks, Ruff, compileall, installer smoke tests, and diff review.
- Orchestrator: not needed for implementation; Pi/Herdr guidance remains optional in the product bundle.
- Max workers / budget: two read-only scouts; no further worker budget assumed.
- Allowed edits / tools / downloads / external calls / deployment: repository edits, cached reference inspection, supplied v0.3 inspection, local validation, and explicit global skill replacement with `--force`; no deployment.
- Explicit approval needed for: remote publishing, paid services, destructive history rewrites, or copied third-party content.

## Tasks
| ID | Vertical output | Owner | Paths/worktree | Depends | Size | Status |
|---|---|---|---|---|---|---|
| T1 | Architecture and scope map | Lead | root metadata and references | none | M | DONE |
| T2 | Original core workflow and product guidance | Lead | `SKILL.md`, `references/`, `templates/` | T1 | M | DONE |
| T3 | Composable promoted skill set and metadata | Lead | `skills/` | T1 | H | DONE |
| T4 | Plugin, handbook, governance, and index files | Lead | `.agents/`, `.claude-plugin/`, `handbook/`, `.github/`, root docs | T3 | H | DONE |
| T5 | Installer and structural validation | Lead | `scripts/`, `package.json` | T2-T4 | M | DONE |
| T6 | Removal, tests, diff review, and delivery | Lead | repository-wide | T5 | M | DONE |

## Evidence and decisions
- Reference architecture: cached public skill repository used as a structural model only.
- Additional input reviewed: the supplied MinimalShip v0.3 bundle, including grilling and orchestration guidance.
- Decision: retain the product-development ideas and Pi/Herdr boundaries, but remove vendor-specific orchestrator instructions and raw/copy-preserving source machinery.
- Decision: use `handbook/` for public docs because `docs/` is local-only in this repository.
- Known limitation: historical Git commits still contain removed source material. This change removes it from the current tree without rewriting shared history.
- Delivery status: baseline bundle merged into `main` as `687de12`; follow-up installer hardening is tracked on a focused branch.
