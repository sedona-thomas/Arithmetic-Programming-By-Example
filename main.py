#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Sedona Thomas
    main.py: finds solutions to the set of inputs using brute force
'''

import sys

class BruteForcePBE(object):

    def __init__(self, file: str = "inputs.txt", limit: int = 10):
        self.examples = {}
        self.solutions = set()
        self.valid = True
        self.scope = range(-limit, limit)
        self.__parse_file(file)

    def solve(self) -> None:
        self.solutions |= {(a, b, c) for a in self.scope for b in self.scope for c in self.scope if self.__is_solution(a, b, c)}

    def save(self, file: str = "solutions.txt") -> None:
        f = open(file, "w")
        if not self.valid:
            f.write("Invalid examples (multiple outputs for the same input)\n")
        for solution in self.solutions:
            f.write(self.__format_expression(solution) + "\n")
        f.close()
        
    def __parse_file(self, file: str) -> None:
        with open(file) as f:
            for line in f:
                li = line.split()
                input, output = int(li[0]), int(li[1])
                if not self.__validate(input, output):
                    self.valid = False
                self.examples[input] = output

    def __validate(self, input: int, output: int) -> bool:
        return self.examples[input] != output if input in self.examples.keys() else True

    def __is_solution(self, a: int, b: int, c: int) -> bool:
        if b == 0:
            return False
        for input in self.examples.keys():
            if (input * a // b + c) != self.examples[input]:
                return False
        return True

    def __format_expression(self, solution: tuple) -> str:
        return "x * {:4} // {:4} + {:4}".format(*solution)

def run():
    solver = BruteForcePBE() if len(sys.argv) < 2 else BruteForcePBE(sys.argv[1], int(sys.argv[2])) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else BruteForcePBE(sys.argv[1])
    solver.solve()
    solver.save()

def run_tests():
    for i in range(1, 4):
        solver = BruteForcePBE("test{}.txt".format(i), int(sys.argv[2])) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else BruteForcePBE("test{}.txt".format(i))
        solver.solve()
        solver.save("test{}_solutions.txt".format(i))

def main():
    if len(sys.argv) > 3: run_tests()
    else: run()
    
if __name__ == '__main__':
    main()