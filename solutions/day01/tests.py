import unittest

from solution import Solution

class Tests(unittest.TestCase):

    def test_shortest_path(self):
        solution = Solution()
        
        self.assertEqual(solution.shortest_path(["R2", "L3"]), 5, 'Oops')
        self.assertEqual(solution.shortest_path(["R2", "R2", "R2"]), 2, 'Oops')
        self.assertEqual(solution.shortest_path(["R5", "L5", "R5", "R3"]), 12, 'Oops')
        
    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, 'Oops')

if __name__ == '__main__':
    unittest.main()