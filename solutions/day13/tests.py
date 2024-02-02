import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        visited = solution.walk_the_maze((1, 1), 10, 1, (7,4))
        self.assertEqual(visited, 11, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()