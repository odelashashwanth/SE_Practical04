
import unittest
from a import get_result

TEST_DATA = [
    ("TC01", 0, "fail"),
    ("TC02", 39, "fail"),
    ("TC03", 40, "pass"),
    ("TC04", 101, "Invalid"),
    ("TC05", 50, "pass"),
    ("TC06", 60, "pass"),
    ("TC07", 75, "pass"),
    ("TC08", 89, "pass"),
    ("TC09", 100, "pass"),
    ("TC10", -1, "Invalid"),
]

class TestResult(unittest.TestCase):
    def test_get_result(self):
        for test_case, marks, expected_result in TEST_DATA:
            with self.subTest(test_case=test_case):
                result = get_result(marks)
                self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)

