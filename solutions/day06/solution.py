# puzzle prompt: https://adventofcode.com/2016/day/6

import sys
sys.path.insert(0, "..")
from base.advent import *
from collections import Counter

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 6

    def get_corrected_message_common(self, messages):
        return "".join(Counter(c).most_common(1)[0][0] for c in zip(*messages))

    def get_corrected_message_uncommon(self, messages):
        return "".join(Counter(c).most_common()[-1][0] for c in zip(*messages))

    def part_1(self):
        res = self.get_corrected_message_common(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_corrected_message_uncommon(self.input)

        self.solve("2", res)


if __name__ == '__main__':
    solution = Solution()

    solution.part_1()

    solution.part_2()
