#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Sedona Thomas
    main.py: finds arithmatic solutions to the set of inputs
'''

import sys
from arith_expr_brute_force_pbe import ArithExprBruteForcePBE
from arith_expr_bottom_up_pbe import ArithExprBottomUpPBE

assignment = 2

number_of_tests = 4
test_file_location = "test_files/test{}.txt"
test_solutions_location = "test_files/test{}_solutions.txt"

def run_assignment_2():
    if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        solver = ArithExprBottomUpPBE(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) > 3 and sys.argv[3].isdigit():
        solver = ArithExprBottomUpPBE(sys.argv[1], 5, int(sys.argv[3]))
    elif len(sys.argv) > 2 and sys.argv[2].isdigit():
        solver = ArithExprBottomUpPBE(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) > 1:
        solver = ArithExprBottomUpPBE(sys.argv[1])
    else:
        solver = ArithExprBottomUpPBE()
    solver.solve()
    solver.save()


def run_assignment_2_tests():
    for i in range(1, number_of_tests + 1):
        if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
            solver = ArithExprBottomUpPBE(test_file_location.format(
                i), int(sys.argv[2]), int(sys.argv[3]))
        elif len(sys.argv) > 3 and sys.argv[3].isdigit():
            solver = ArithExprBottomUpPBE(test_file_location.format(i), 2, int(sys.argv[3]))
        elif len(sys.argv) > 2 and sys.argv[2].isdigit():
            solver = ArithExprBottomUpPBE(test_file_location.format(i), int(sys.argv[2]))
        else:
            solver = ArithExprBottomUpPBE(test_file_location.format(i))
        solver.solve()
        solver.save(test_solutions_location.format(i))


def run_assignment_1():
    if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        solver = ArithExprBruteForcePBE(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) > 3 and sys.argv[3].isdigit():
        solver = ArithExprBruteForcePBE(sys.argv[1], 5, int(sys.argv[3]))
    elif len(sys.argv) > 2 and sys.argv[2].isdigit():
        solver = ArithExprBruteForcePBE(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) > 1:
        solver = ArithExprBruteForcePBE(sys.argv[1])
    else:
        solver = ArithExprBruteForcePBE()
    solver.solve()
    solver.save()


def run_assignment_1_tests():
    for i in range(1, number_of_tests + 1):
        if len(sys.argv) > 3 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
            solver = ArithExprBruteForcePBE(test_file_location.format(
                i), int(sys.argv[2]), int(sys.argv[3]))
        elif len(sys.argv) > 3 and sys.argv[3].isdigit():
            solver = ArithExprBruteForcePBE(test_file_location.format(i), 2, int(sys.argv[3]))
        elif len(sys.argv) > 2 and sys.argv[2].isdigit():
            solver = ArithExprBruteForcePBE(test_file_location.format(i), int(sys.argv[2]))
        else:
            solver = ArithExprBruteForcePBE(test_file_location.format(i))
        solver.solve()
        solver.save(test_solutions_location.format(i))


def main():
    if assignment == 1:
        if len(sys.argv) > 4:
            run_assignment_1_tests()
        else:
            run_assignment_1()
    elif assignment == 2:
        if len(sys.argv) > 4:
            run_assignment_2_tests()
        else:
            run_assignment_2()

if __name__ == '__main__':
    main()
