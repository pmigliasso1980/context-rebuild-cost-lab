# Decisions

## D-001 — Use only the Python standard library at runtime

**Status:** accepted on 2026-11-24

The lab measures context rebuild cost, not package-download speed. A
dependency-free runtime makes clean startup deterministic, inexpensive, and
possible offline. `setuptools` is only required for editable installation;
verification can run directly with `PYTHONPATH=src`.

## D-002 — Measure from a clean Git archive

**Status:** accepted on 2026-11-24

The measurement script exports committed `HEAD` into a new temporary directory.
It then follows the fresh-session commands without using the working tree,
untracked files, caches, or an existing virtual environment. This isolates
documented rebuild cost from prior local state.

## D-003 — Treat three minutes as the diagnostic threshold

**Status:** accepted on 2026-11-24

An elapsed rebuild above 180 seconds triggers a concrete documentation or
workflow improvement and a second comparable run. A faster run is still
reported with limitations; no unnecessary adjustment is invented.

