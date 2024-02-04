# puzzle prompt: https://adventofcode.com/2016/day/16

import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 16


    def checksum(self, initial_state, length):
        table = str.maketrans("01", "10")
        
        state = initial_state

        while len(state) < length:
            new = state[::-1].translate(table)
            state = f"{state}0{new}"

        check = state[:length]

        while not len(check) % 2:
            check = [int(x == y) for x, y in zip(*[iter(check)]*2)]

        return "".join(map(str, check))


    def part_1(self):
        res = self.checksum(self.input, 272)

        self.solve("1", res)

    def part_2(self):
        res = self.checksum(self.input, 35_651_584)

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()