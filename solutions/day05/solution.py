# puzzle prompt: https://adventofcode.com/2016/day/5

from itertools import count
from hashlib import md5
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 5

    def get_password(self, door_id):
        pwd = ""

        for i in count():
            digest = md5(f"{door_id}{i}".encode()).hexdigest()
            if digest.startswith("00000"):
                pwd += digest[5]
                if len(pwd) == 8:
                    return pwd


    def get_password_positioned(self, door_id):
        pwd = {}

        for i in count():
            digest = md5(f"{door_id}{i}".encode()).hexdigest()
            if digest.startswith("00000"):
                if digest[5] not in {"0", "1", "2", "3", "4", "5", "6", "7"}:
                    continue

                check = int(digest[5])

                if check in pwd:
                    continue

                pwd[check] = digest[6]

                if len(pwd) == 8:
                    return "".join([v for k, v in sorted(pwd.items())])
                
    def part_1(self):
        res = self.get_password(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_password_positioned(self.input)

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()