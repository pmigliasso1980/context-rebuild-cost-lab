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

The clean-context rebuild completed successfully in **3.0476 seconds**, against
the lab threshold of 180 seconds.

### Method

On 2026-11-24, `scripts/measure_rebuild.py` performed the following measured
procedure on macOS arm64 with Python 3.11.3:

1. Export committed `HEAD` with `git archive`.
2. Extract it into a newly created temporary directory.
3. Read and validate the startup anchors in `AGENTS.md`, `PROGRESS.md`,
   `DECISIONS.md`, and `README.md`.
4. Create a new isolated virtual environment with no reused `.venv`.
5. Run the full `unittest` suite against `src/`.
6. Run the CLI smoke check and require a zero exit status.

The procedure deliberately excludes the working tree, untracked files, old
virtual environments, and dependency caches from the project. It includes Git
export, context reading, environment creation, tests, and the smoke check.

| Step | Seconds |
|---|---:|
| Export committed `HEAD` | 0.0220 |
| Extract clean checkout | 0.0034 |
| Read initialization context | 0.0002 |
| Create isolated environment | 2.8341 |
| Run test framework | 0.0487 |
| Run CLI smoke check | 0.0310 |
| **End-to-end total** | **3.0476** |

Machine-readable evidence is committed at
[`evidence/rebuild-measurement.json`](evidence/rebuild-measurement.json).
Reproduce it with:

```bash
python3 scripts/measure_rebuild.py --output evidence/rebuild-measurement.json
```

### Diagnostic and adjustment decision

Creating the virtual environment accounted for roughly 93% of elapsed time;
context discovery was effectively negligible. The 3.0476-second total is
176.9524 seconds below the intervention threshold. Therefore no corrective
change to `AGENTS.md`, `PROGRESS.md`, or `DECISIONS.md` was required after the
reset. Avoiding an unnecessary second mechanism keeps the rebuild path simpler.

The main limitation is that this is one local run on a small dependency-free
project. It measures deterministic rebuild mechanics, not network clone latency
or third-party package download time.

## Git workflow

The commit history records the work in evaluation order:

1. Runnable environment and initial tests.
2. Startup checklist, task breakdown, and decisions.
3. Reproducible rebuild measurement tooling.
4. Measured evidence and analysis.

