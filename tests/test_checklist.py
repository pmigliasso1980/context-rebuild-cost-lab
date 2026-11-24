import unittest

from readiness.checklist import Check, readiness_summary


class ReadinessSummaryTests(unittest.TestCase):
    def test_all_checks_pass(self) -> None:
        ready, failed = readiness_summary(
            [Check("environment", True), Check("tests", True)]
        )

        self.assertTrue(ready)
        self.assertEqual([], failed)

    def test_failed_check_is_reported(self) -> None:
        ready, failed = readiness_summary(
            [Check("environment", True), Check("documentation", False)]
        )

        self.assertFalse(ready)
        self.assertEqual(["documentation"], failed)


if __name__ == "__main__":
    unittest.main()
