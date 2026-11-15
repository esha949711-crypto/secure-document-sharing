"""Runs the suite and writes tests/TEST_REPORT.md (expected vs actual table)."""
import datetime, platform, sys, unittest
import cryptography
from tests import test_sdsp

class R(unittest.TextTestResult):
    def __init__(s, *a, **k): super().__init__(*a, **k); s.rows = []
    def _row(s, t, actual):
        doc = t.shortDescription().split("|"); s.rows.append((doc[0].strip(), doc[1].strip(), doc[2].strip(), actual))
    def addSuccess(s, t): super().addSuccess(t); s._row(t, "PASS")
    def addFailure(s, t, e): super().addFailure(t, e); s._row(t, "FAIL")
    def addError(s, t, e): super().addError(t, e); s._row(t, "ERROR")

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_sdsp)
    res = unittest.TextTestRunner(resultclass=R, verbosity=1).run(suite)
    lines = ["# Test Report", "",
             f"- Date: {datetime.date.today()}  |  Python {platform.python_version()}  |  cryptography {cryptography.__version__}",
             f"- Result: **{res.testsRun - len(res.failures) - len(res.errors)}/{res.testsRun} passed**", "",
             "| ID | Test | Expected | Actual |", "|---|---|---|---|"]
    lines += [f"| {i} | {d} | {e} | {a} |" for i, d, e, a in sorted(res.rows, key=lambda r: (int("".join(c for c in r[0] if c.isdigit())), r[0]))]
    open("tests/TEST_REPORT.md", "w").write("\n".join(lines) + "\n")
    sys.exit(0 if res.wasSuccessful() else 1)
