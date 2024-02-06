# puzzle prompt: https://adventofcode.com/2016/day/17

import sys
sys.path.insert(0,"..")

from base.advent import *
from itertools import compress
from collections import deque
from hashlib import md5

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 17

    moves = {
        "U": ( 0, -1),
        "D": ( 0,  1),
        "L": (-1,  0),
        "R": ( 1,  0)
    }

    def is_open(self, passcode, vertex, dirs):
        chars = md5(f"{passcode}{dirs}".encode()).hexdigest()[:4]
        for direction, (dx, dy) in compress(self.moves.items(), (c in "bcdef" for c in chars)):
            next = (vertex[0] + dx, vertex[1] + dy)
            if 0 <= next[0] <= 3 and 0 <= next[1] <= 3: #inbounds
                yield direction, next


    def walk_the_rooms(self, passcode):
        start = (0, 0)
        end = (3, 3)
        queue = deque([(start, "")])
        while queue:
            vertex, directions = queue.popleft()
            for direction, next in self.is_open(passcode, vertex, directions):
                if next == end:
                    yield directions + direction
                else:
                    queue.append((next, directions + direction))

    def part_1(self):
        directions = list(self.walk_the_rooms(self.input))
        res = directions[0]

        self.solve("1", res)

    def part_2(self):
        directions = list(self.walk_the_rooms(self.input))
        res = len(directions[-1])

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()