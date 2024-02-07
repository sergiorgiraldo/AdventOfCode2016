import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solution.get_lucky_elf(5), 3, "Oops")

    def test_part2(self):
        self.assertEqual(solution.get_lucky_elf_across_circle(5), 2, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()