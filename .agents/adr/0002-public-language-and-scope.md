# ADR 0002: Publish original English product-development guidance

- Status: accepted
- Date: 2026-10-22
- Owners: MinimalShip contributors

## Context

The earlier bundle mixed copied source archives, Vietnamese public pages, and unrelated startup material. That created legal, maintenance, and scope noise.

## Decision

Rewrite the retained principles and workflows in original English, keep only product-development content, and remove raw sources, translations, line indexes, and unrelated startup advice from the current tree. Historical Git commits are not rewritten by this change.

## Alternatives considered

- Preserve source archives with hashes: strong provenance, but republishes material the product does not own and keeps stale content alive.
- Publish bilingual copies: useful in some contexts, but conflicts with the current public-language requirement.
- Keep all startup topics: broadens the product beyond the problem it is meant to solve.

## Consequences

The package is smaller and independently authored. Historical source material remains visible only in prior Git history, not in the current installable tree.

## Evidence and review trigger

Revisit if the product scope changes or a licensed, user-requested translation is added as a separate, reviewed package.
