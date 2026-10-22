# Mocking boundaries

Mock only a boundary that is slow, nondeterministic, expensive, private, or owned by another system. Do not mock the module under test or replace the business rule with a mock.

Prefer a small fake when the interaction has meaningful state. Prefer contract tests when an external API shape matters. Keep mock data realistic and assert the observable outcome, not the number of internal calls unless call count is itself a contract.
