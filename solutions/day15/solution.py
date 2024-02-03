# puzzle prompt: https://adventofcode.com/2016/day/15

import sys
sys.path.insert(0,"..")

import re
from itertools import count
from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 15

    def get_discs(self, lines, extra_disc=False):
        discs = []

        digits = re.compile(r"(\d+)") #Disc #2 has 2 positions; at time=0, it is at position 1.
        
        for line in lines:
            _, num_positions, _, start_pos = map(int, digits.findall(line))
            discs.append((num_positions, start_pos))

        if extra_disc:
            discs.append((11, 0))

        return discs

    def get_capsule(self, lines, extra_disc=False):
        discs = self.get_discs(lines, extra_disc)

        for i in count():
            for t, (mod, start) in enumerate(discs, 1):
                if (start + t + i) % mod != 0:
                    break
            else: #https://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html
                return i

    def part_1(self):
        res = self.get_capsule(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_capsule(self.input, True)

        self.solve("2", res)

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()