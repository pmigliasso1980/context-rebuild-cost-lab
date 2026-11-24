# Progress

Last updated: 2026-11-24

## Startup-readiness checklist

- [x] Repository initialized on `main`.
- [x] Python 3.11+ requirement is explicit.
- [x] Runtime dependencies are declared (none).
- [x] Editable-install command is documented.
- [x] Test discovery command is documented and passing.
- [x] At least one test proves useful behavior.
- [x] CLI smoke check is documented and passing.
- [x] Generated files and secrets are ignored.
- [x] Rebuild measurement procedure is defined.
- [ ] Fresh-checkout measurement recorded.
- [ ] Public GitHub remote published and verified.

## Ordered task breakdown

1. **Environment** — initialize Git, declare Python/package configuration, and
   ignore generated local files. Status: complete.
2. **Verification** — implement one behavior and a deterministic test suite.
   Status: complete (2 tests).
3. **Context** — document setup, readiness, constraints, decisions, and work
   order. Status: complete.
4. **Measurement** — rebuild from a clean archive in an empty temporary
   directory and record elapsed wall-clock time. Status: pending.
5. **Diagnosis** — if elapsed time exceeds 180 seconds, improve an
   initialization artifact and rerun the same procedure. Status: pending.
6. **Publication** — push the staged commit history to a public GitHub
   repository and verify file links. Status: pending.

## Current handoff

Start at `AGENTS.md`. Do not infer task state from Git history alone; this file
is the live handoff. The next action is task 4, measurement.

