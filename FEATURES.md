# MinimalShip feature inventory

This inventory tracks the current bundle and the v0.5 major update. `EXISTING VERIFIED` rows describe behavior already observed; `REQUESTED` rows describe the upgrade being executed now. `RUN.md` contains only the active cycle, ownership, evidence and resume checkpoint.

| ID | Origin | Feature | User value / purpose | Priority | Complexity | Status | Dependencies | Acceptance criteria | Owner |
|---|---|---|---|---|---|---|---|---|---|
| F1 | EXISTING VERIFIED | Composable root plus 27 promoted skills | Discover the smallest useful workflow or discipline without loading a monolith | MUST | H | DONE | none | Fresh installation exposes `/skill:minimalship` and all 27 promoted names | lead |
| F2 | EXISTING VERIFIED | Flat Pi installation and conflict protection | Install skills without hiding promoted commands or overwriting unrelated paths silently | MUST | M | DONE | F1 | Profile and project smoke installs pass; conflicts require `--force` | lead |
| F3 | EXISTING VERIFIED | Private profile boundary | Keep personal preferences and permissions outside the public bundle | MUST | M | DONE | F1 | Public templates are neutral; separate profile status and installation checks pass | lead |
| F4 | EXISTING VERIFIED | Understand-to-plan state checkpoint | Research a project and leave a compact, resumable feature inventory and run record before execution | MUST | M | DONE | F1 | Workflow smoke check confirms ordered phases, `FEATURES.md`, `RUN.md` and approval gate | lead |
| F5 | EXISTING VERIFIED | Optional profile with scoped execution gates | Let normal work continue with neutral defaults while protecting risky actions | MUST | M | DONE | F3 | Profile smoke check passes optional, partial, strict and permissions/dispatch cases | lead |
| F6 | EXISTING VERIFIED | Atomic installer replacement and regression coverage | Avoid broken partial installs when a forced replacement fails | MUST | M | DONE | F2 | Installer rollback, project/profile, unrelated-path and link-safety checks pass | lead |
| F7 | REQUESTED | Behavioral E01–E08 evaluation harness | Prove that the workflow changes agent behavior instead of only checking document wording | MUST | M | VERIFYING | F4, F5 | Eight scenario fixtures run through the live adapter when supported; deterministic graders emit structured PASS/FAIL/BLOCKED results and compare baseline fields | lead |
| F8 | REQUESTED | Opt-in stack-aware external routing and QA gates | Select only relevant official Cloudflare, Expo/EAS or Vercel guidance without changing the project's stack or causing side effects | MUST | M | DONE | F1, F4 | Evidence-based route detector passes positive and negative cases; routing never auto-installs, vendors, upgrades, deploys or charges; stack QA gates are explicit | lead |
| F9 | REQUESTED | Repeatable Pi/Herdr, ownership and resume verification | Distinguish filesystem smoke from real runtime evidence and recover work without repeating settled decisions | MUST | M | VERIFYING | F4, F7 | Runtime report verifies available Pi/Herdr surfaces or records BLOCKED; task-envelope, overlap, false-completion and resume fixtures pass deterministically | lead |
| F10 | REQUESTED | Required READ-to-ITERATE workflow contract | Keep the minimal workflow names, checkpoint fields and approval boundary consistent across core docs and templates | MUST | M | DONE | F4, F7, F8 | Root sequence is READ → CLARIFY → FEATURES → SPEC → PLAN → APPROVE → DISPATCH → BUILD → VERIFY → SHIP → ITERATE; `RUN.md` has a resume checkpoint; existing checks remain green | lead |

## Status rule

A feature is `DONE` only when every required acceptance criterion above has executed evidence in `RUN.md`. A failed, unexecuted or blocked criterion keeps the feature in `VERIFYING` or `BLOCKED`; worker claims and plans are not evidence.
