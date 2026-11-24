# AGENTS.md

## Purpose

This repository measures how cheaply a fresh contributor can rebuild project
context. The product itself is a dependency-free Python startup-readiness
checker; the lab evidence is recorded in `PROGRESS.md` and `README.md`.

## Stack

- Python 3.11 or newer
- Standard-library `unittest`
- `setuptools` only when installing the package
- No runtime third-party dependencies

## Fresh-session startup

Run these commands from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/readiness-check
```

For an offline verification that does not install anything:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m readiness.cli
```

## Definition of ready

A checkout is ready when:

1. Python is at least version 3.11.
2. The virtual environment exists when installation is required.
3. All tests pass.
4. The CLI prints `READY: all startup checks passed` and exits zero.
5. `git status --short` is empty after verification.

## Constraints

- Keep the runtime dependency-free unless a recorded decision changes this.
- Keep business logic in `src/readiness/`; tests belong in `tests/`.
- Never commit `.venv`, caches, credentials, or generated temporary clones.
- Update `PROGRESS.md` when task status or rebuild measurements change.
- Update `DECISIONS.md` when a durable technical choice changes.
- Run tests and the CLI before every commit.

## Authoritative files

- Current state, checklist, ordered work: [`PROGRESS.md`](PROGRESS.md)
- Durable choices and tradeoffs: [`DECISIONS.md`](DECISIONS.md)
- Rebuild method and findings: [`README.md`](README.md)
- Package configuration: [`pyproject.toml`](pyproject.toml)
- Executable verification: [`tests/test_checklist.py`](tests/test_checklist.py)

