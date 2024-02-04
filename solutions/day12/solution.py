# puzzle prompt: https://adventofcode.com/2016/day/12

import sys
sys.path.insert(0, "..")
from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 12

    def interpret(self, input, regs):
        def val(x): return (regs[x] if x in regs else x)

        code = [self.parse(line) for line in input]

        current = 0

        while current < len(code):
            instruction = code[current]
            op, x, y = instruction[0], instruction[1], instruction[-1]
            current += 1
            if op == "cpy":
                regs[y] = val(x)
            elif op == "inc":
                regs[x] += 1
            elif op == "dec":
                regs[x] -= 1
            elif op == "jnz" and val(x):
                current += y - 1
        return regs

    def parse(self, line):
        return tuple((x if x.isalpha() else int(x))
                     for x in line.split())

    def part_1(self):
        regs = self.interpret(self.input, dict(a=0, b=0, c=0, d=0))
        res = regs["a"]

        self.solve("1", res)

    def part_2(self):
        regs = self.interpret(self.input, dict(a=0, b=0, c=1, d=0))
        res = regs["a"]

        self.solve("2", res)


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()