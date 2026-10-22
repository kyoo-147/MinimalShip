# MinimalShip feature inventory

This inventory tracks the current bundle and this refinement cycle. `EXISTING VERIFIED` rows describe behavior already observed before this branch; `REQUESTED` rows describe the refinement being verified now.

| ID | Origin | Feature | User value / purpose | Priority | Complexity | Status | Dependencies | Acceptance criteria | Owner |
|---|---|---|---|---|---|---|---|---|---|
| F1 | EXISTING VERIFIED | Composable root plus 27 promoted skills | Discover the smallest useful workflow or discipline without loading a monolith | MUST | H | DONE | none | Fresh installation exposes `/skill:minimalship` and all 27 promoted names | lead |
| F2 | EXISTING VERIFIED | Flat Pi installation and conflict protection | Install skills without hiding promoted commands or overwriting unrelated paths silently | MUST | M | DONE | F1 | Profile and project smoke installs pass; conflicts require `--force` | lead |
| F3 | EXISTING VERIFIED | Private profile boundary | Keep personal preferences and permissions outside the public bundle | MUST | M | DONE | F1 | Public templates are neutral; separate profile status and installation checks pass | lead |
| F4 | REQUESTED | Understand-to-plan state checkpoint | Research a project and leave a compact, resumable feature inventory and run record before execution | MUST | M | DONE | F1 | Workflow smoke check confirms ordered phases, `FEATURES.md`, `RUN.md` and approval gate | lead |
| F5 | REQUESTED | Optional profile with scoped execution gates | Let normal work continue with neutral defaults while protecting risky actions | MUST | M | DONE | F3 | Profile smoke check passes optional, partial, strict and permissions/dispatch cases | lead |
| F6 | REQUESTED | Atomic installer replacement and regression coverage | Avoid broken partial installs when a forced replacement fails | MUST | M | DONE | F2 | Installer rollback, project/profile, unrelated-path and link-safety checks pass | lead |

## Status rule

A feature is `DONE` only when every acceptance criterion above has executed evidence in `RUN.md`. A release or merge blocker may still remain in `RUN.md` without changing a feature's product status.
