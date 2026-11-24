# Context Rebuild Cost Lab

This public lab repository demonstrates a complete initialization phase and a
measured context rebuild after a clean reset. Its small product is a Python CLI
that reports whether startup-readiness checks pass.

## Initialization outputs

1. [Agent startup instructions](AGENTS.md)
2. [Startup checklist and ordered task breakdown](PROGRESS.md)
3. [Initial test framework](tests/test_checklist.py)
4. [Project configuration](pyproject.toml)

Durable choices and measurement controls are in [DECISIONS.md](DECISIONS.md).

## Setup and verification

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/readiness-check
```

The runtime has no third-party dependencies. For the cheapest offline check:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m readiness.cli
```

## Initialization phase

The Git history intentionally separates the runnable baseline, context
artifacts, measurement tooling, and measured results. This makes the order of
operations and the reason for each change reviewable.

## Rebuild-cost findings

Measurement has not run yet. The committed measurement procedure will replace
this section with the environment, exact method, elapsed time, outcome, and any
threshold-triggered adjustment.

