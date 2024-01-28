# puzzle prompt: https://adventofcode.com/2016/day/7
import re
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 7

    def has_ABBA(self, s):
        return any(w[:2] == w[3:1:-1] and w[0] != w[1]
                for w in zip(s, s[1:], s[2:], s[3:]))


    def get_ABA(self, s):
        return [w for w in zip(s, s[1:], s[2:]) if w[0] == w[2] != w[1]]


    def get_ips_with_TLS(self, arg):
        count = 0
        for ip in arg:
            sections = re.split(r"(\[.*?])", ip)
            sup, hypernet = sections[::2], sections[1::2]
            count += any(map(self.has_ABBA, sup)) and not any(map(self.has_ABBA, hypernet))

        return count


    def get_ips_with_SSL(self, arg):
        count = 0
        for ip in arg:
            sections = re.split(r"(\[.*?])", ip)
            sup, hypernet = sections[::2], sections[1::2]
            babs = {b + a + b for x in sup for a, b, a in self.get_ABA(x)}
            count += any(bab in x for bab in babs for x in hypernet)

        return count

    def part_1(self):
        res = self.get_ips_with_TLS(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_ips_with_SSL(self.input)

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()