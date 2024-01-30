# puzzle prompt: https://adventofcode.com/2016/day/9
import re
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 9

    pattern = re.compile(r'\((\d+)x(\d+)\)')

    def get_decompressed_string(self, input):
        arg = input

        pos = 0
        while True:
            match = self.pattern.search(arg, pos)
            if match is None:
                break
            chars, num = map(int, match.groups())
            start, end = match.start(), match.end()
            arg = arg[:start] + arg[end:end+chars] * num + arg[end+chars:]
            pos = start + chars * num

        return arg

    def get_decompressed_string_v2(self, arg):
        while True:
            match = self.pattern.search(arg)
            if match is None:
                yield len(arg)
                return

            chars, num = map(int, match.groups())
            end = match.end()

            yield match.start() + sum(self.get_decompressed_string_v2(arg[end:end+chars])) * num

            arg = arg[end+chars:]
        
    def part_1(self):
        arg = self.get_decompressed_string(self.input)

        res = len(arg)

        self.solve("1", res)

    def part_2(self):
        arg = self.input

        res = sum(self.get_decompressed_string_v2(arg))

        self.solve("2", res)

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()