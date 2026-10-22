# MinimalShip grill contract

## Modes

- **Quick**, the default: one compact round covering only missing outcome, MUST / NOT NOW scope, acceptance and the next decision. Ask execution policy, budget and permissions only when implementation or dispatch is authorized or being considered.
- **Deep**, explicit or risk-triggered: a dependency-ordered decision tree for product, architecture, and safety choices.

## Decision frontier

Build a private tree:

`outcome -> user journey -> constraints -> acceptance -> approval -> execution -> release risk`

Ask only questions whose prerequisites are settled. The agent should inspect facts from the repository and tools. The user owns product choices, trade-offs, authority, and irreversible effects.

## Round format

```text
Q1 - <decision>: <concrete question>
Recommended: <one answer and why>

Q2 - ...
```

Record settled answers once in `RUN.md`, then prune them from later rounds. Do not ask the user to inspect a file the agent can read. Do not use an interview to postpone a reversible local choice.

## Exit condition

Stop when the user journey is unambiguous, MUST and NOT NOW are explicit, three to seven acceptance cases have concrete input/action/output, the demo environment is known, and worker/model/permission policy is resolved. Close with one short acceptance contract. Any remaining high-risk unknown is BLOCKED, not silently assumed.
