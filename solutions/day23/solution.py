# puzzle prompt: https://adventofcode.com/2016/day/23

import sys
sys.path.insert(0,"..")
from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 23

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

        registers = dict(a=7, b=0, c=0, d=0)

        res = self.run(code, registers)

        self.solve("1", res["a"])

    def part_2(self):
        code = [self.parse(line) for line in self.input]

        registers = dict(a=12, b=0, c=0, d=0)

        res = self.run(code, registers) #took 14 minutes!

        self.solve("2", res["a"])

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()