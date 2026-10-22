# ADR 0001: Use a composable bundle around a stable root skill

- Status: accepted
- Date: 2026-10-22
- Owners: MinimalShip contributors

## Context

MinimalShip began as one Pi workflow. The product now needs focused disciplines that can be discovered and reused without loading a large monolithic prompt, while the `/skill:minimalship` entry point must remain stable.

## Decision

Keep the root `SKILL.md` as the Pi workflow and add promoted skills under engineering and productivity buckets. Give each promoted skill its own metadata, handbook page, index entry, and manifest entry. Keep public repository pages under `handbook/` because `docs/` is local-only.

## Alternatives considered

- Keep one large skill: simplest distribution, but poor reuse and context control.
- Copy a reference repository wholesale: more surface area and copied assumptions than MinimalShip needs.
- Build a hosted registry: out of scope and unnecessary for local installation.

## Consequences

The checker must validate cross-file consistency. The installer copies a larger public tree. New skills need a distinct boundary and evidence before promotion.

## Evidence and review trigger

Revisit if Pi cannot use the root workflow, if metadata drifts across harnesses, or if the promoted set becomes harder to understand than the original problem.
