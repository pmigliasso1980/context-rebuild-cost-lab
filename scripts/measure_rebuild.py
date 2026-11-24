#!/usr/bin/env python3
"""Measure a documented rebuild from committed HEAD in an empty directory."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import subprocess
import tempfile
import time
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    """Run a required rebuild step and fail loudly on an error."""

    subprocess.run(command, cwd=cwd, env=env, check=True, capture_output=True, text=True)


def measure() -> dict[str, object]:
    started = time.perf_counter()
    steps: list[dict[str, object]] = []

    def timed_step(name: str, action: object) -> None:
        step_started = time.perf_counter()
        action()  # type: ignore[operator]
        steps.append({"name": name, "seconds": round(time.perf_counter() - step_started, 4)})

    with tempfile.TemporaryDirectory(prefix="context-rebuild-") as temporary:
        temp = Path(temporary)
        archive = temp / "head.zip"
        checkout = temp / "checkout"

        timed_step(
            "export committed HEAD",
            lambda: run(
                ["git", "archive", "--format=zip", "HEAD", "-o", str(archive)], ROOT
            ),
        )
        timed_step(
            "extract clean checkout",
            lambda: (checkout.mkdir(), zipfile.ZipFile(archive).extractall(checkout)),
        )

        def read_context() -> None:
            required = {
                "AGENTS.md": "## Fresh-session startup",
                "PROGRESS.md": "## Ordered task breakdown",
                "DECISIONS.md": "## D-002",
                "README.md": "## Setup and verification",
            }
            for filename, marker in required.items():
                content = (checkout / filename).read_text(encoding="utf-8")
                if marker not in content:
                    raise RuntimeError(f"{filename} lacks required marker: {marker}")

        timed_step("read initialization context", read_context)
        timed_step(
            "create isolated environment",
            lambda: run(["python3", "-m", "venv", ".venv"], checkout),
        )

        env = os.environ.copy()
        env["PYTHONPATH"] = str(checkout / "src")
        python = checkout / ".venv" / "bin" / "python"
        timed_step(
            "run test framework",
            lambda: run(
                [str(python), "-m", "unittest", "discover", "-s", "tests", "-v"],
                checkout,
                env,
            ),
        )
        timed_step(
            "run CLI smoke check",
            lambda: run([str(python), "-m", "readiness.cli"], checkout, env),
        )

    elapsed = round(time.perf_counter() - started, 4)
    return {
        "method": "git archive HEAD into a new temporary directory; read context; create venv; run tests and CLI",
        "python": platform.python_version(),
        "platform": platform.platform(),
        "elapsed_seconds": elapsed,
        "threshold_seconds": 180,
        "within_threshold": elapsed <= 180,
        "result": "pass",
        "steps": steps,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON evidence path")
    args = parser.parse_args()
    result = measure()
    rendered = json.dumps(result, indent=2) + "\n"
    print(rendered, end="")
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

