# Review checklist

- Spec and acceptance: is the requested behavior present and bounded?
- User path: does the real input-to-result journey work?
- Error path: are invalid input, timeouts, permissions, and partial failure handled?
- Tests: do they protect public seams and meaningful regressions?
- Design: does the change deepen a module or spread policy into callers?
- Security: are secrets, trust boundaries, shell calls, and external inputs safe?
- Operations: are migrations, logs, retries, timeouts, and rollback concerns explicit?
- Scope: are unrelated refactors and speculative abstractions absent?
