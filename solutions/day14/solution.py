# puzzle prompt: https://adventofcode.com/2016/day/14

import sys
sys.path.insert(0, "..")

import re
from itertools import islice
from functools import lru_cache
from base.advent import *
from hashlib import md5

BIG = 10 ** 999


class Solution(InputAsStringSolution):
    _year = 2016
    _day = 14

    @lru_cache(1001)
    def hashval(self, i, salt, stretch):
        h = md5(bytes(salt + str(i), "utf-8")).hexdigest()
        if not stretch:
            return h
        else:
            for i in range(stretch):
                h = md5(bytes(h, "utf-8")).hexdigest()
            return h

    def is_key(self, i, salt, stretch):
        "A key has a triple like `777`, and then `77777` in one of the next thousand hashval(i)."
        three = re.search(r"(.)\1\1", self.hashval(i, salt, stretch))
        if three:
            five = three.group(1) * 5
            return any(five in self.hashval(i+delta, salt, stretch) for delta in range(1, 1001))

    def nth(self, iterable, n, default=None):
        "Returns the nth item of iterable, or a default value"
        return next(islice(iterable, n, None), default)

    def nth_key(self, N, salt, stretch):
        return self.nth(filter(lambda i: self.is_key(i, salt, stretch), range(BIG)), N)

    def part_1(self):
        salt = self.input
        res = self.nth_key(63, salt, None)

        self.solve("1", res)

    def part_2(self):
        salt = self.input
        res = self.nth_key(63, salt, 2016)

        self.solve("2", res)


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
