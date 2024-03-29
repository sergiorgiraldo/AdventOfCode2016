# puzzle prompt: https://adventofcode.com/2016/day/1

import sys
sys.path.insert(0, "..")
from base.advent import *


class Solution(InputAsStringSolution):
    _year = 2016
    _day = 1

    def shortest_path(self, instructions):
        faceX, faceY = 0, 1
        x, y = 0, 0
        for instruction in instructions:
            direction, offset = instruction[0], int(instruction[1:])
            faceX, faceY = (
                faceY, -faceX) if direction == 'R' else (-faceY, faceX)
            x += faceX * offset
            y += faceY * offset

        return abs(x) + abs(y)

    def first_duplicate(self, instructions):
        faceX, faceY = 0, 1
        x, y = 0, 0
        locations = {(x, y)}

        for instruction in instructions:
            direction, offset = instruction[0], int(instruction[1:])
            faceX, faceY = (
                faceY, -faceX) if direction == 'R' else (-faceY, faceX)

            for _ in range(offset):
                x += faceX
                y += faceY
                if (x, y) not in locations:
                    locations.add((x, y))
                else:
                    return abs(x) + abs(y)

        return abs(x) + abs(y)

    def part_1(self):
        arr = self.input.split(", ")
        res = self.shortest_path(arr)

        self.solve("1", res)

    def part_2(self):
        arr = self.input.split(", ")
        res = self.first_duplicate(arr)

        self.solve("2", res)


if __name__ == "__main__":
    solution = Solution()
    solution.part_1()
    solution.part_2()
