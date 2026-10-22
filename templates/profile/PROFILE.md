# MinimalShip private profile

This file belongs to the person or team using MinimalShip.
It is a private preference and policy layer, not part of the public skill bundle.
Keep it outside any public repository.

## Status

- status: incomplete
- profile_id: ?
- profile_owner: ?
- default_language: ?
- profile_root: ?
- last_reviewed: ?

A `?` means unknown. Ordinary project work may continue with neutral defaults, but a profile cannot be applied as complete until its required fields and modules are explicit.
`not applicable` and `use neutral defaults` are valid explicit answers.

## Modules

- [ ] `VOICE.md` - communication style and response format.
- [ ] `OPINIONS.md` - decision preferences and trade-offs.
- [ ] `BUILD_PLAYBOOK.md` - preferred product and engineering loop.
- [ ] `TASTE_UI.md` - visual and interaction preferences.
- [ ] `RESEARCH_TASTE.md` - research evidence and writing rules.
- [ ] `UI_TESTING.md` - visual, responsive, accessibility and state coverage.
- [ ] `ORCHESTRATION.md` - agent, worker and runtime boundaries.
- [ ] `PERMISSIONS.md` - tools, network, credentials, cloud and deployment policy.

## Source policy

Do not copy a personal profile into the public MinimalShip repository.
Do not commit credentials, tokens, private paths, recovery archives or machine-specific settings.
The public bundle provides neutral templates and a question list only.

## Runtime contract

- No profile: continue safe local inspection and planning with neutral defaults.
- Partial profile: apply only explicit values; ask only for a missing preference or execution boundary that matters to the current action.
- Complete profile: apply the completed modules without exposing their contents.
- Before worker dispatch or external effects, require explicit execution policy or a one-time approval. Do not infer permissions from silence.

## Completion rule

A profile is complete only when every required module has an explicit answer, the checklist is checked, and no required field remains `?` or blank.
Use `python scripts/profile-status.py --require profile` for the strict full-profile check.
Use `--require permissions` or `--require dispatch` when only an execution boundary must be resolved.
