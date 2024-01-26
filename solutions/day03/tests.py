import unittest

from solution import Solution

class Tests(unittest.TestCase):
    def test_triangles_by_rows(self):
        solution = Solution()
        self.assertEqual(solution.get_valid_triangles_By_rows([(5, 10, 25), (3, 4, 5), (5, 12, 13)]), 2, "Oops")

    def test_triangles_by_columns(self):
        solution = Solution()
        self.assertEqual(solution.get_valid_triangles_By_columns([(5, 3, 12), (10, 4, 13), (25, 5, 5)]), 2, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()