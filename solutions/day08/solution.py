# puzzle prompt: https://adventofcode.com/2016/day/8
import re
import sys
sys.path.insert(0,"..")
from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 8

    def display(self, instructions):
        screen = [[0] * 6 for _ in range(50)]

        for instruction in instructions:
            if instruction.startswith("rect"):
                x, y = map(int, re.split("[ x]", instruction)[1:])
                for j in range(x):
                    for k in range(y):
                        screen[j][k] = 1
            else:
                c, v = map(int, re.split("(?: by |=)", instruction)[-2:])
                if "x=" in instruction:
                    screen[c] = screen[c][-v:] + screen[c][:-v]
                else:
                    t = [list(x) for x in zip(*screen)]
                    t[c] = t[c][-v:] + t[c][:-v]
                    screen = [list(x) for x in zip(*t)]

        return screen

    def part_1(self):
        screen = self.display(self.input)
        res = sum(sum(x) for x in screen)

        self.solve("1", res)

    def part_2(self):
        screen = self.display(self.input)
        for row in zip(*screen):
            print("".join(" #"[i] for i in row))

#  # ###   ##    ## #### #    ###   ##  #### #### 
#  # #  # #  #    # #    #    #  # #  # #       # 
#  # #  # #  #    # ###  #    ###  #    ###    #  
#  # ###  #  #    # #    #    #  # #    #     #   
#  # #    #  # #  # #    #    #  # #  # #    #    
 ##  #     ##   ##  #    #### ###   ##  #### ####         
        
        res = "UPOJFLBCEZ"

        self.solve("2", res)

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()