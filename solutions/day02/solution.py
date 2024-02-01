# puzzle prompt: https://adventofcode.com/2016/day/2

from base.advent import *
import sys
sys.path.insert(0, "..")


class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 2

    def get_bathroom_code(self, instructions):
        keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

        keypad, code = [*zip(*keypad[::-1])], []

        for instruction in instructions:
            x, y = code[-1] if code else (1, 1)
            for step in instruction:
                tx = x + (step in 'LR' and (-1) ** (step == 'L'))
                ty = y + (step in 'UD' and (-1) ** (step == 'D'))
                try:
                    if tx < 0 or ty < 0:
                        raise IndexError
                    keypad[tx][ty]
                except IndexError:
                    continue
                else:
                    x, y = tx, ty

            code.append((x, y))

        code_keys = [keypad[x][y] for x, y in code]

        code = "".join(str(key) for key in code_keys)

        return code

    def get_bathroom_code_cross(self, instructions):
        keypad = [
            [..., ..., 1, ..., ...],
            [..., 2, 3, 4, ...],
            [5, 6, 7, 8, 9],
            [..., 'A', 'B', 'C', ...],
            [..., ..., 'D', ..., ...]]

        keypad, code = [*zip(*keypad[::-1])], []

        for instruction in instructions:
            x, y = code[-1] if code else (0, 2)
            for step in instruction:
                tx = x + (step in 'LR' and (-1) ** (step == 'L'))
                ty = y + (step in 'UD' and (-1) ** (step == 'D'))

                try:
                    if tx < 0 or ty < 0 or keypad[tx][ty] is ...:
                        raise IndexError
                except IndexError:
                    continue
                else:
                    x, y = tx, ty

            code.append((x, y))

        code_keys = [keypad[x][y] for x, y in code]

        code = "".join(str(key) for key in code_keys)

        return code

    def part_1(self):
        res = self.get_bathroom_code(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_bathroom_code_cross(self.input)

        self.solve("2", res)


if __name__ == '__main__':
    solution = Solution()
    solution.part_1()
    solution.part_2()
