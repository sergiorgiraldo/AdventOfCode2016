# puzzle prompt: https://adventofcode.com/2016/day/4

import sys
import string
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 4

    def get_sector_real_rooms(self, rooms):
        sum = 0
        for room in rooms:                  # e.g udglrdfwlyh-gbh-ilqdqflqj-439[otyms]
            *name, last = room.split("-")   # udglrdfwlyh-gbh-ilqdqflqj / 439[otyms]
            id, check = last.split("[")     # 439 / otyms]
            sector = "".join(name)          # udglrdfwlyhgbhilqdqflqj
            checksum = sorted({*sector}, key=lambda x: (-sector.count(x), x))
            if checksum[:5] == [*check.strip("]")]:
                sum += int(id)

        return sum

    def get_sector_north_pole(self, rooms):
        for room in rooms:
            *name, last = room.split("-")
            id = int(last.split("[")[0])
            for word in name:
                decrypted = self.decrypt(word, id)
                if "north" in decrypted:
                    return id

    def decrypt(self, cypher, id):
        return "".join(string.ascii_lowercase[(ord(c) - ord("a") + id) % 26] for c in cypher)

    def part_1(self):
        res = self.get_sector_real_rooms(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.get_sector_north_pole(self.input)

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()