import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solution.nth_key(63, "abc", None), 22_728, "Oops")

    def test_part2(self):
        self.assertEqual(solution.nth_key(63, "abc", 2016), 22_551, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()