import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        program = [
            "cpy 2 a",
            "tgl a",
            "tgl a",
            "tgl a",
            "cpy 1 a",
            "dec a",
            "dec a"
        ]
        code = [solution.parse(line) for line in program]

        registers = dict(a=0, b=0, c=0, d=0)

        res = solution.run(code, registers)

        self.assertEqual(res["a"], 3, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()