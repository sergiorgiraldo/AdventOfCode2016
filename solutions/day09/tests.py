import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(len(solution.get_decompressed_string("ADVENT")), 6, "Oops")
        self.assertEqual(len(solution.get_decompressed_string("A(1x5)BC")), 7, "Oops")
        self.assertEqual(len(solution.get_decompressed_string("(3x3)XYZ")), 9, "Oops")
        self.assertEqual(len(solution.get_decompressed_string("A(2x2)BCD(2x2)EFG")), 11, "Oops")
        self.assertEqual(len(solution.get_decompressed_string("(6x1)(1x3)A")), 6, "Oops")
        
    def test_part2(self):
        self.assertEqual(sum(solution.get_decompressed_string_v2("(3x3)XYZ")), 9, "Oops")
        self.assertEqual(sum(solution.get_decompressed_string_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A")), 241_920, "Oops")
        self.assertEqual(sum(solution.get_decompressed_string_v2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")), 445, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == '__main__':
    unittest.main()