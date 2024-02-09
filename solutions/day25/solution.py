# puzzle prompt: https://adventofcode.com/2016/day/25

import sys
sys.path.insert(0,"..")

from base.advent import *
from collections import Counter
from itertools import count

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 25

    def run(self, code, registers):
        def val(x): return (registers[x] if x in registers else x)
            
        current = 0

        while 0 <= current < len(code):
            instruction = code[current]
            op, x, y = instruction[0], instruction[1], instruction[-1]
            current += 1
            if   op == "cpy" and y in registers: registers[y] = val(x)
            elif op == "inc":               registers[x] += 1                  
            elif op == "dec":               registers[x] -= 1                  
            elif op == "jnz" and val(x):    current += val(y) - 1   
            elif op == "tgl":               self.toggle(code, current - 1 + val(x))
            elif op == "out":               yield val(x)
        return registers

    def toggle(self, code, i):
        if 0 <= i < len(code): 
            instruction = code[i]
            instruction[0] = (
                    "dec" if instruction[0] == "inc"   else 
                    "inc" if len(instruction) == 2     else
                    "cpy" if instruction[0] == "jnz"   else 
                    "jnz")

    def parse(self, line): 
        return [(x if x.isalpha() else int(x)) 
                for x in line.split()]

    def part_1(self):
        code = [self.parse(line) for line in self.input]

        for i in count():
            if all(x == y 
                   for x, y in 
                   zip(self.run(code, dict(a=i, b=0, c=0, d=0)), (0, 1) * 10)): #10 seems a good repeating pattern
                res = i
                break

        self.solve("1", res)

    def part_2(self):
        pass

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()