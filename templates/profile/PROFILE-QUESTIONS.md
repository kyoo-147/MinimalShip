# MinimalShip profile questions

Answer every question with a concrete value, `not applicable`, or `use neutral defaults`.
Do not infer answers from a name, repository, previous session, or personal archive.
Do not complete this catalog before ordinary project inspection or planning. P01-P07 and P10 are optional preference and recovery context. Resolve P08 only when worker dispatch is being considered and P09 only when the current action needs a permission boundary. A one-time explicit approval may replace a missing private answer for a single local action.

## P01. Profile and context

1. What local profile name should the agent use?
2. Which language should the agent use for conversation and public artifacts?
3. Which name, organization, or project context may be used, if any?
4. Where should the private profile live?

## P02. Voice

1. Should responses be concise, detailed, or adaptive?
2. Which tone should the agent use?
3. Which languages, honorifics, punctuation rules, or formatting conventions matter?
4. Which claims, labels, or phrases must the agent avoid?

## P03. Engineering opinions

1. What priorities should resolve trade-offs between correctness, simplicity, reliability, security, maintainability, performance and speed?
2. What coding, naming, documentation and commit rules should apply?
3. What evidence is required before calling work complete?
4. Which practices are prohibited?

## P04. Build playbook

1. How should the agent understand the problem before choosing architecture?
2. When should it reuse, extend, customize or build from scratch?
3. What is the preferred smallest complete vertical slice?
4. Which deterministic tools should be preferred over AI?
5. When should models, services, queues, databases or infrastructure be introduced?

## P05. Product and research opinions

1. What user outcome matters most for product work?
2. Which trade-offs deserve pushback instead of automatic agreement?
3. Which measures distinguish useful progress from activity?
4. Which claims require primary-source evidence or reproducible experiments?

## P06. UI taste

1. What is the visual direction, hierarchy and density preference?
2. Which typography, color, icon, spacing, radius and motion rules apply?
3. Which UI patterns are discouraged?
4. Which states and difficult data must always be shown?

## P07. UI testing

1. Which real user journey must be tested?
2. Which browsers, devices, viewports or automation tools are available?
3. Which loading, empty, error, success and disabled states are required?
4. Which accessibility, responsive and reference-fidelity checks are mandatory?

## P08. Orchestration

1. Which agent host, model providers, thinking modes and speed modes are allowed?
2. Is a worker orchestrator allowed, and which one is primary?
3. What are the worker, budget, concurrency and worktree limits?
4. Which files, interfaces or tasks require single ownership?

## P09. Permissions and safety

1. May the agent edit files, install packages, download tools or use network access?
2. May it access credentials, cloud dashboards, paid APIs or production systems?
3. Which actions require confirmation, review, rollback or a human-only wizard?
4. Which data must never be stored, logged or committed?

## P10. Handoff and recovery

1. What checkpoint file should preserve decisions across compaction, fork, resume or handoff?
2. What must be recorded after a blocked or failed run?
3. Who owns unresolved decisions when the user is unavailable?
