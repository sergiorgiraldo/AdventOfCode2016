import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    #no test cases this day
    
    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()