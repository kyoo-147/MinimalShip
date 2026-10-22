# Profile boundary

MinimalShip separates the public workflow from the private preferences of the person or team using it.

## Three layers

1. **Public bundle**: neutral English instructions, templates, question lists, metadata and validation.
2. **Private operator profile**: voice, opinions, build playbook, UI taste, research taste, testing, orchestration and permission rules.
3. **Project state**: repository instructions, `RUN.md`, decisions, code, tests and project-specific constraints.

The public repository must not contain a person's name, private voice, machine paths, credentials, recovery archive or unverified personal configuration.

## Separate runtime profile

A dedicated Pi profile can use its own agent directory.
The directory may contain the MinimalShip skill, private profile files and profile-local settings without mixing them with another agent setup.

```powershell
py .\scripts\init-profile.py --agent-dir "$env:USERPROFILE\.pi\profiles\minimalship"
py .\scripts\install.py --profile "$env:USERPROFILE\.pi\profiles\minimalship" --force
$env:PI_CODING_AGENT_DIR = "$env:USERPROFILE\.pi\profiles\minimalship"
$env:MINIMALSHIP_PROFILE_DIR = "$env:USERPROFILE\.pi\profiles\minimalship\profile"
py .\scripts\profile-status.py
pi
```

The profile initializer only creates blank templates.
It never imports a personal archive, downloads dependencies or writes credentials.

## Resolution order

When a profile-aware run starts, resolve the private profile in this order:

1. `MINIMALSHIP_PROFILE_DIR`, when explicitly set.
2. The `profile` directory under `PI_CODING_AGENT_DIR`.
3. A project-local `.minimalship/profile` only when the project explicitly opts in.
4. No profile.

A profile from one user or machine must never be silently reused for another project or person.

## First-run gate

If the profile is absent, marked `incomplete`, or contains unanswered `?` values, stop before applying personal preferences.
Use `python scripts/profile-status.py` to perform the deterministic readiness check when the helper is installed.
Report:

```text
BLOCKED: PROFILE_INCOMPLETE
```

Then list every unanswered question from `templates/profile/PROFILE-QUESTIONS.md`.
The user may answer the questions, choose `use neutral defaults`, or mark a section `not applicable`.
The agent must not infer personal preferences from a name, previous session, recovery folder or unrelated repository.

After the user answers, write the completed profile only to the private profile directory.
Do not write answers back into the public MinimalShip package.

## Completion rule

A profile is complete when every required module has an explicit answer and no required field remains `?`.
A project may still have its own unresolved product questions in `RUN.md`.
Those are separate from the operator profile and must be asked by the normal MinimalShip workflow.
