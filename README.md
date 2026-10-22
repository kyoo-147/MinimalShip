# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

MinimalShip is a product-building workspace grounded in real user needs: start with a specific problem, ship the smallest valuable version, and continuously improve it through user feedback and real-world data.

It is also the shared space for developing our products, reusable skills, tools, and working practices.

## Product philosophy

### Build what matters

- Start with a real problem, not a feature list or a fashionable technology.
- Understand who the users are, what they struggle with, and how they solve it today.
- Serve a specific group of users well before expanding.
- Give every feature a clear reason to exist and a way to validate its value.

### Ship what works

- Release the smallest version that solves a complete, meaningful need.
- Keep the scope small without compromising the quality of the core experience.
- Work in short cycles; split work that cannot be completed within one cycle.
- Test the critical paths and protect against regressions before release.
- Do manual work early when it helps us understand the problem; automate once the bottleneck is clear.

### Improve what users need

- Reach out to, support, and listen to early users directly.
- Combine qualitative feedback with usage data instead of relying on assumptions.
- Measure the outcomes users achieve, not the number of features we ship.
- Improve, remove, or expand features based on new evidence.

## How we work

**Understand the problem → Choose the goal → Build the smallest useful version → Test → Ship → Measure and listen → Improve.**

Each cycle has one primary goal. Before starting a piece of work, make the following clear:

1. **User and problem:** Who needs this? What specific difficulty are we addressing?
2. **Desired outcome:** What should be better when this is done?
3. **Scope:** What is essential, and what can wait?
4. **Ownership:** Who is responsible for completing it?
5. **Definition of done:** How will we test it and measure its impact?

Priorities change as we learn during each cycle rather than being locked to a long-term roadmap.

## Shared product principles

- **Focus:** Every product has a clear core value.
- **Usability:** Remove unnecessary steps and help users complete their work.
- **Reliability:** Shipping quickly never replaces testing, data safety, and operational readiness.
- **Enough is enough:** Choose the simplest solution that meets the current need; add complexity only when it earns its place.

## Code, skills, and documentation

The repository contains source code, reusable skills, and the guidance needed to work on the project.
The repository contains source code, reusable skills, and the guidance needed to work on the project.

## MinimalShip Workflow

This repository includes the **MinimalShip workflow skill**, a prototype-first product development system for Pi Coding Agent and Herdr. It keeps work focused on a clear outcome, a small runnable slice, bounded worker orchestration, and evidence-based verification.

- `SKILL.md` — the operational workflow
- `templates/RUN.md` — the compact spec, plan, task, and QA record
- `references/` — orchestration guidance and product principles
- `sources/` — preserved reference material with SHA-256 verification
- `scripts/check.py` — integrity and structure checks
- `scripts/install.py` — project or global installation

Install it globally on Windows with `py .\\scripts\\install.py --global`, then invoke it in Pi with `/skill:minimalship`.

Reference material, research notes, and working analyses are **kept local only** and must not be committed or pushed. The `docs/`, `analysis/`, and `.local/` directories are ignored by Git for this purpose.

## Status

The project is currently establishing its foundation. No product, technology stack, or application run command has been defined in the repository yet.

Setup, development, and testing instructions will be added alongside the first product implementation.
