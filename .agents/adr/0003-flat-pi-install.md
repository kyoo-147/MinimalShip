# ADR 0003: Install promoted skills as flat Pi siblings

- Status: accepted
- Date: 2026-10-22
- Owners: MinimalShip contributors

## Context

Pi's recursive skill loader treats a directory containing `SKILL.md` as a skill root and stops descending into that directory. Installing the root bundle at `skills/minimalship/` with promoted skills nested below it therefore exposes only `/skill:minimalship`.

## Decision

Keep the complete root bundle at `skills/minimalship/` for its references, templates and maintenance metadata. During installation, copy each promoted skill directory to a sibling path under the same Pi skill directory, such as `skills/implement/` and `skills/grill-me/`. The installer checks every destination before changing anything and requires `--force` to replace an existing root or promoted path.

The symlink helper follows the same layout. It reports conflicts by default, supports `--check` for a read-only preflight, and removes an existing destination only when `--force` is explicit.

## Consequences

Pi can discover `/skill:minimalship` plus all 27 promoted commands through its normal recursive loader. Installations use more sibling directories and may conflict with another skill using the same name; deliberate replacement is explicit. The root bundle contains a duplicate source tree under `skills/`, which preserves documentation and source reviewability without affecting Pi discovery.

## Evidence and review trigger

The disposable smoke test must verify all 28 installed `SKILL.md` files, conflict preservation without `--force`, and deliberate replacement with `--force`. A local Pi loader probe must report the root plus all 27 promoted skill names. Revisit if Pi adds an official package registration mechanism that makes flat installation unnecessary.
