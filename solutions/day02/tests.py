import unittest

from solution import Solution

class Tests(unittest.TestCase):
    def test_get_bathroom_code_simple(self):
        arr = ["ULL", "RRDDD", "LURDL", "UUUUD"]
        solution = Solution()
        self.assertEqual(solution.get_bathroom_code(arr), "1985", "Oops")

    def test_get_bathroom_code_hard(self):
        arr = ["ULL", "RRDDD", "LURDL", "UUUUD"]
        solution = Solution()
        self.assertEqual(solution.get_bathroom_code_cross(arr), "5DB3", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()