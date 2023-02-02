#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Sedona Thomas
    main.py: finds arithmatic solutions to the set of inputs using brute force
'''

import sys
from arith_expr_pbe import ArithExprPBE


def run():
    if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        solver = ArithExprPBE(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) > 3 and sys.argv[3].isdigit():
        solver = ArithExprPBE(sys.argv[1], 5, int(sys.argv[3]))
    elif len(sys.argv) > 2 and sys.argv[2].isdigit():
        solver = ArithExprPBE(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) > 1:
        solver = ArithExprPBE(sys.argv[1])
    else:
        solver = ArithExprPBE()
    solver.solve()
    solver.save()


def run_tests():
    number_of_tests = 4
    for i in range(1, number_of_tests + 1):
        if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
            solver = ArithExprPBE("test{}.txt".format(
                i), int(sys.argv[2]), int(sys.argv[3]))
        elif len(sys.argv) > 3 and sys.argv[3].isdigit():
            solver = ArithExprPBE("test{}.txt".format(i), 2, int(sys.argv[3]))
        elif len(sys.argv) > 2 and sys.argv[2].isdigit():
            solver = ArithExprPBE("test{}.txt".format(i), int(sys.argv[2]))
        else:
            solver = ArithExprPBE("test{}.txt".format(i))
        solver.solve()
        solver.save("test{}_solutions.txt".format(i))


def main():
    if len(sys.argv) > 4:
        run_tests()
    else:
        run()


if __name__ == '__main__':
    main()
