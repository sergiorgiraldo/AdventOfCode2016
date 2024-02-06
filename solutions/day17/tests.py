import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        directions = list(solution.walk_the_rooms("ihgpwlah"))
        self.assertEqual(directions[0], "DDRRRD", "Oops")

        directions = list(solution.walk_the_rooms("kglvqrro"))
        self.assertEqual(directions[0], "DDUDRLRRUDRD", "Oops")

        directions = list(solution.walk_the_rooms("ulqzkmiv"))
        self.assertEqual(directions[0], "DRURDRUDDLLDLUURRDULRLDUUDDDRR", "Oops")

    def test_part2(self):
        directions = list(solution.walk_the_rooms("ihgpwlah"))
        self.assertEqual(len(directions[-1]), 370, "Oops")

        directions = list(solution.walk_the_rooms("kglvqrro"))
        self.assertEqual(len(directions[-1]), 492, "Oops")

        directions = list(solution.walk_the_rooms("ulqzkmiv"))
        self.assertEqual(len(directions[-1]), 830, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
