# MinimalShip feature inventory — <project>

Keep this file as the product inventory. Use `RUN.md` for the current cycle and execution checkpoint.

| ID | Origin | Feature | User value / purpose | Priority | Complexity | Status | Dependencies | Acceptance criteria | Owner |
|---|---|---|---|---|---|---|---|---|---|
| F1 | EXISTING VERIFIED | <observed capability> | <who benefits and why> | MUST | E | DONE | none | <evidence-backed criterion> | <owner or unassigned> |
| F2 | REQUESTED | <new capability> | <who benefits and why> | MUST | M | TODO | F1 | <input → action → expected result> | <owner or unassigned> |

## Field rules

- **Origin:** use `EXISTING VERIFIED` only for behavior observed in the repository or an executed check; use `REQUESTED` for newly requested scope.
- **Priority:** `MUST`, `NICE` or `NOT NOW`.
- **Complexity:** `E`, `M` or `H`.
- **Status:** `TODO`, `READY`, `IN_PROGRESS`, `VERIFYING`, `DONE` or `BLOCKED`.
- **Dependencies:** list feature IDs or `none`.
- **Acceptance criteria:** keep them concrete and testable.
- **Owner:** one person or agent when assigned; otherwise `unassigned`.

A feature may become `DONE` only after every required acceptance criterion has executed evidence. A failed, unexecuted or blocked criterion keeps the feature in `VERIFYING` or `BLOCKED`.
