# puzzle prompt: https://adventofcode.com/2016/day/19

import sys
sys.path.insert(0,"..")

from base.advent import *
import collections

class Solution(InputAsStringSolution):
    _year = 2016
    _day = 19

    # part 1 is a solution to the Josephus problem
    # https://en.wikipedia.org/wiki/Josephus_problem
    # https://www.youtube.com/watch?v=uCsD3ZGzMgE
    def get_lucky_elf(self, group_size):
        return int("0b" + bin(group_size)[3:] + "1", 2)

#  Odd ########################
#   1
# 5   2
#  4 3
 
#   1           1
# 5   2  -->  5   2
#  4 -          4
 
#   1         1 
# -   2  -->     2
#   4         4 
 
#  -          2  
#     2  -->
#  4          4
 
#  2
#     -->  2  
#  -          
#  Even ########################
#   1
# 6   2
# 5   3
#   4 
  
#   1
# 6   2 
#  5 3
 
#   1           1
# -   2  -->  5   2
#  5 3          3
 
#   -           2 
# 5   2  -->  5
#   3           3 

#    5          5  
# 2      -->
#    -          2
 
#  -
#     -->  2  
#  2


    def get_lucky_elf_across_circle(self, group_size):
        left = collections.deque()
        right = collections.deque()
        for i in range(1, group_size + 1):
            if i < (group_size // 2) + 1:
                left.append(i)
            else:
                right.appendleft(i)

        while left and right:
            if len(left) > len(right):
                left.pop()
            else:
                right.pop()

            # rotate
            right.appendleft(left.popleft())
            left.append(right.pop())
        return left[0] or right[0]

    def part_1(self):
        res = self.get_lucky_elf(int(self.input))

        self.solve("1", res)

    def part_2(self):
        res = self.get_lucky_elf_across_circle(int(self.input))

        self.solve("2", res)

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()