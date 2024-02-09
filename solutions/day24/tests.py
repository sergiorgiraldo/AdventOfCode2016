import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        map = [
            "###########",
            "#0.1.....2#",
            "#.#######.#",
            "#4.......3#",
            "###########"          
        ]
        self.assertEqual(solution.walk_the_map(map), 14, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()