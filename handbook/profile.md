# Private profiles and first-run setup

MinimalShip is public and neutral by design.
Personal voice, opinions, UI taste, research habits, runtime preferences and permission rules belong in a separate private profile.

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

## First use

If the profile is incomplete, MinimalShip does not pretend to know the operator's preferences.
It reports `BLOCKED: PROFILE_INCOMPLETE` and lists the unanswered questions.

Answer with a concrete value, `not applicable`, or `use neutral defaults`.
The completed answers remain outside the public repository.

## Public/private rule

Commit neutral templates and the question catalog.
Do not commit personal names, private paths, credentials, recovery archives, voice rules, opinions or machine-specific settings.
Project-specific product decisions still belong in the consuming repository's `RUN.md`, instructions and ADRs.
