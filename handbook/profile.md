# Private profiles and first-run setup

MinimalShip is public and neutral by design.
Personal voice, opinions, UI taste, research habits, runtime preferences and permission rules belong in an optional private profile.

## Create a separate profile

```powershell
py .\scripts\init-profile.py --agent-dir "$env:USERPROFILE\.pi\profiles\minimalship"
py .\scripts\install.py --profile "$env:USERPROFILE\.pi\profiles\minimalship" --force
$env:PI_CODING_AGENT_DIR = "$env:USERPROFILE\.pi\profiles\minimalship"
$env:MINIMALSHIP_PROFILE_DIR = "$env:USERPROFILE\.pi\profiles\minimalship\profile"
py .\scripts\profile-status.py
pi
```

The initializer creates blank files under the selected agent directory.
Fill them only after reviewing `PROFILE-QUESTIONS.md`.

## Normal project work

A missing or partial profile does not block safe project inspection, clarification, specification or local planning.
MinimalShip uses neutral defaults for unresolved preferences and asks only when a missing preference changes the current decision.

```text
PASS: PROFILE_OPTIONAL   # no configured profile
PASS: PROFILE_PARTIAL    # selected profile is incomplete
PASS: PROFILE_COMPLETE   # all preference modules are explicit
```

The completed profile remains outside the public repository.

## Execution boundaries

Permissions and dispatch policy are checked only when the current action needs them:

```powershell
py .\scripts\profile-status.py --require permissions
py .\scripts\profile-status.py --require dispatch
```

An unresolved required boundary returns `BLOCKED` and names only that boundary. A one-time explicit approval can resolve a local action without completing unrelated voice, UI, research or style questions.

Use the strict full-profile gate only when the operator explicitly wants personal preferences applied everywhere:

```powershell
py .\scripts\profile-status.py --require profile
```

## Public/private rule

Commit neutral templates and the question catalog.
Do not commit personal names, private paths, credentials, recovery archives, voice rules, opinions or machine-specific settings.
Project-specific product decisions belong in the consuming repository's `FEATURES.md`, `RUN.md`, instructions and ADRs.
