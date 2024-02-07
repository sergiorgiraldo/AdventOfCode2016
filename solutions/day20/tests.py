import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        ip_list = ["5-8", "0-2", "4-7"]
        self.assertEqual(solution.get_allowed(ip_list, 9)[0], 3, "Oops")

    def test_part2(self):
        ip_list = ["5-8", "0-2", "4-7"]
        self.assertEqual(solution.get_allowed(ip_list, 9)[1], 2, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()