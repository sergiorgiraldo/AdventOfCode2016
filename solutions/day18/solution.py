# puzzle prompt: https://adventofcode.com/2016/day/18

import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 18

    def get_safe_tiles(self, initial_tiles, rows):
        prev, safes = initial_tiles, initial_tiles.count(".")
        for _ in range(rows - 1):
            padded = f".{prev}." # left from 0 and right from -1 are non-existent and always safe
            prev = "".join(".^"[left != right] for left, _, right in zip(padded, padded[1:], padded[2:]))
            safes += prev.count(".")

        return safes

    def part_1(self):
        res = self.get_safe_tiles(self.input, 40)

        self.solve("1", res)

    def part_2(self):
        res = self.get_safe_tiles(self.input, 400_000)

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()