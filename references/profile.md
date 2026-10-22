# Profile boundary

MinimalShip separates the public workflow from private operator preferences and execution policy.

## Three layers

1. **Public bundle**: neutral English instructions, templates, question lists, metadata and validation.
2. **Private operator profile**: optional voice, opinions, build playbook, UI taste, research taste, testing, orchestration and permission rules.
3. **Project state**: repository instructions, `FEATURES.md`, `RUN.md`, decisions, code, tests and project-specific constraints.

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

## Optional preference layer

A missing profile is not a project blocker.
Continue safe repository inspection, clarification, specification and local planning with neutral defaults.
A partial profile is also not a global blocker: apply only explicit values and ask only for a missing preference that affects the current decision.
Never infer private preferences from a name, previous session, recovery archive or unrelated repository.

`python scripts/profile-status.py` reports `PASS: PROFILE_OPTIONAL`, `PASS: PROFILE_PARTIAL`, or `PASS: PROFILE_COMPLETE` for this normal path.

## Scoped execution gates

Permissions and worker policy are different from optional style preferences.
Before an action that needs them, use the narrowest check:

```powershell
py .\scripts\profile-status.py --require permissions
py .\scripts\profile-status.py --require dispatch
```

If the required boundary is unresolved, report a scoped `BLOCKED` result and ask for only that decision, or obtain a one-time explicit approval.
Do not require unrelated voice, UI, research or style answers before ordinary development.

## Full profile check

When the user explicitly wants a completed personal profile, use:

```powershell
py .\scripts\profile-status.py --require profile
```

That strict command reports `BLOCKED: PROFILE_INCOMPLETE` and lists the profile questions when the selected profile is incomplete.
Answers belong only in the private profile directory and never in the public MinimalShip package.
