# puzzle prompt: https://adventofcode.com/2016/day/10

import sys
sys.path.insert(0, "..")
from base.advent import *
from collections import defaultdict


class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 10

    def factory(self, instructions, part, comparison=None):
        product_of_chips = 1
        bots, instruction = defaultdict(list), {}

        for current in instructions:
            split = [int(x) if x.isdigit() else x for x in current.split()]
            if current.startswith("value"):  # value 5 goes to bot 2
                bots[split[-1]] += split[1],
            else:                           # bot 2 gives low to bot 1 and high to bot 0
                instruction[split[1]] = (
                    split[5], split[6], split[-2], split[-1])

        while True:
            id = next((k for k, v in bots.items() if len(v) > 1), None)
            if id is None:
                break

            low, lowId, high, highId = instruction[id]
            m, M = sorted(bots.pop(id))
            if part == 1:
                if (m, M) == comparison:
                    return id

            if low == "bot":
                bots[lowId] += m,
            else:
                if lowId in {0, 1, 2}:
                    product_of_chips *= m

            if high == "bot":
                bots[highId] += M,
            else:
                if highId in {0, 1, 2}:
                    product_of_chips *= M

        if part == 2:
            return product_of_chips

    def part_1(self):
        res = self.factory(self.input, 1, (17, 61))

        self.solve("1", res)

    def part_2(self):
        res = self.factory(self.input, 2)

        self.solve("2", res)


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
