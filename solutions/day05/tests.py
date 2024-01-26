import unittest

from solution import Solution

class Tests(unittest.TestCase):

    def test_get_password(self):
        solution = Solution()
        self.assertEqual(solution.get_password("abc"), "18f47a30", "Oops")

    def test_get_password_positioned(self):
        solution = Solution()
        self.assertEqual(solution.get_password_positioned("abc"), "05ace8e3", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()