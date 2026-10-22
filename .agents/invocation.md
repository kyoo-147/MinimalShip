# Invocation metadata

MinimalShip has two kinds of promoted skill:

## User-invoked

Use for routers, setup, interviews, planning, implementation, and other orchestration. These skills include `disable-model-invocation: true` in `SKILL.md` and `allow_implicit_invocation: false` in `agents/openai.yaml`.

## Model-invoked

Use for reusable disciplines such as testing, diagnosis, module design, research, review, and authoring. These skills have a trigger-oriented description and no explicit-invocation restriction.

Keep metadata synchronized. A mismatch is a distribution bug because one harness may invoke a skill implicitly while another treats it as an explicit command.
