"""Validation logic for a small startup-readiness checklist."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    """One named readiness condition."""

    name: str
    passed: bool


def readiness_summary(checks: list[Check]) -> tuple[bool, list[str]]:
    """Return overall readiness and the names of failed checks."""

    failed = [check.name for check in checks if not check.passed]
    return not failed, failed

