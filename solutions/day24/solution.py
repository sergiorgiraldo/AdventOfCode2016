# puzzle prompt: https://adventofcode.com/2016/day/24

import sys
sys.path.insert(0,"..")

from base.advent import *
from itertools import permutations, combinations
from collections import deque

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 24

    def bfs(self, map, start, end):
        queue = deque([(start, 0)])
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = {start}

        while queue:
            vertex, path = queue.popleft()
            if vertex == end:
                return path

            for nxt in ((vertex[0] + i, vertex[1] + j) for i, j in moves):
                if nxt[0] < 0 or nxt[1] < 0 or nxt[0] >= len(map) or nxt[1] >= len(map[0]):
                    continue

                if map[nxt[0]][nxt[1]] != '#' and nxt not in visited:
                    queue.append((nxt, path + 1))
                    visited.add(nxt)

    def walk_the_map(self, map, should_return=False):     
        paths = {}
        
        nums = {int(x): (i, j) for i, y in enumerate(map)
                                for j, x in enumerate(y) if x.isdigit()}

        for a, b in combinations(sorted(nums), 2):
            paths[a, b] = paths[b, a] = self.bfs(map, nums[a], nums[b])

        perms = list(permutations(range(1, len(nums))))

        steps = min(sum(paths[x] for x in zip((0,) + p,  p + (0,) if should_return else p)) for p in perms)

        return steps
    
    def part_1(self):
        res = self.walk_the_map(self.input, False)

        self.solve("1", res)

    def part_2(self):
        res = self.walk_the_map(self.input, True)

        self.solve("2", res)

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()