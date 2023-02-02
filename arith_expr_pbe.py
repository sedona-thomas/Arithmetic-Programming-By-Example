
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Sedona Thomas
    arith_expr_pbe.py: handles solving arithmatic solutions by example using brute force
'''


class ArithExprPBE(object):

    def __init__(self, file: str = "inputs.txt", max_depth: int = 2, max_int: int = 10):
        self.non_terminals = {
            "({}) + {}": int,
            "({}) - {}": int,
            "({}) * {}": int,
            "({}) // {}": int
        }
        self.terminals = {"x"} | {str(i) for i in range(max_int)}
        self.max_depth = max_depth
        self.one_to_one = True
        self.solutions = set()
        self.examples = {}
        self.__parse_file(file)

    def solve(self) -> None:
        for i in range(self.max_depth):
            self.__expand_terminals()
        self.solutions |= {expr
                           for expr in self.terminals
                           if self.__is_solution(expr)
                           }

    def save(self, file: str = "solutions.txt") -> None:
        f = open(file, "w")
        if not self.one_to_one:
            f.write("Invalid examples (multiple outputs for the same input)\n")
        for solution in self.solutions:
            f.write(solution + "\n")
        f.close()

    def __parse_file(self, file: str) -> None:
        with open(file) as f:
            for line in f:
                li = line.split()
                input, output = int(li[0]), int(li[1])
                if not self.__is_one_to_one(input, output):
                    self.one_to_one = False
                self.examples[input] = output

    def __expand_terminals(self):
        self.terminals |= {non_terminal.format(terminal_a, terminal_b)
                           for non_terminal in self.non_terminals
                           for terminal_a in self.terminals
                           for terminal_b in self.terminals
                           }

    def __is_solution(self, expr: str) -> bool:
        try:
            for input in self.examples.keys():
                if eval(expr.replace("x", str(input))) != self.examples[input]:
                    return False
            return True
        except ZeroDivisionError:
            return False

    def __is_one_to_one(self, input: int, output: int) -> bool:
        return self.examples[input] != output if input in self.examples.keys() else True
