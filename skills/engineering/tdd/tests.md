# Test seams

A test seam is a public boundary where behavior can be observed without reaching into private representation. Prefer a real user journey, public function, HTTP boundary, command, or adapter contract over a private helper.

## A useful test

- Names a behavior, not an implementation detail.
- Uses an independent expected result.
- Exercises one meaningful path and one important failure path.
- Fails for the regression it is meant to prevent.
- Leaves the next refactor free to change internals.

When a seam is unclear, stop and use `codebase-design` before adding a test that freezes the wrong shape.
