"""Command-line demonstration of the readiness checker."""

from readiness.checklist import Check, readiness_summary


def main() -> int:
    checks = [
        Check("environment", True),
        Check("tests", True),
        Check("documentation", True),
    ]
    ready, failed = readiness_summary(checks)
    if ready:
        print("READY: all startup checks passed")
        return 0
    print(f"NOT READY: failed checks: {', '.join(failed)}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

