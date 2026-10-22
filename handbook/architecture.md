# Bundle architecture

MinimalShip keeps one stable root workflow and a set of focused promoted skills.

## Root workflow

`SKILL.md` is installed as `/skill:minimalship`. It owns the Understand → Clarify → Specify → Plan → Approve → Dispatch → Build → Verify → Ship → Improve loop, output contract, Pi and Herdr boundary guidance, optional profile behavior and the default Quick mode. The installer keeps this root bundle intact for its references and templates.

## Promoted skills

`skills/engineering` and `skills/productivity` contain focused `SKILL.md` files. Each is independently discoverable and has an `agents/openai.yaml` metadata file. The installer copies each promoted directory as a sibling of `minimalship/`, because Pi stops descending when it finds a `SKILL.md` at a directory root. User-invoked skills are explicit; model-invoked skills are reusable disciplines.

## Public documentation

`handbook/` is the maintained public reading surface. `docs/`, `analysis/`, and `.local/` remain ignored local working areas. The package does not need a tracked docs generator or hosted documentation site to be useful.

## Project state

`templates/FEATURES.md` defines the product inventory when a project needs explicit feature tracking. It distinguishes existing verified capabilities from requested work and owns priority, complexity, status, dependencies, acceptance criteria and owner.

`templates/RUN.md` defines the current-cycle checkpoint. It owns the objective, confirmed decisions, bounded scope, approved execution policy, task ownership, active workers, evidence, blockers and exact next action. The root workflow does not create a duplicate status or backlog file by default.

## Promotion contract

A new promoted skill needs a distinct product-development failure, an original body, metadata, a handbook page, bucket and root indexes, plugin manifest entry, and structural checks. It should not become a thin alias for another skill or a new project-management system.

## Composition

Prefer explicit skill names in user-facing instructions. Model-invoked disciplines may recommend a focused sibling skill, but they should not silently execute user-invoked orchestration. This keeps the call graph visible and prevents duplicate plans.
