# Brute-Force-Programming-By-Example

Determines all valid combinations of addition, subtraction, multiplication, and division within a specified range for given examples. "arith_expr_pbe.py" contains the ArithExprPBE class which "main.py" uses to generate these equations.

`python main.py [optional file] [optional maximum search depth] [optional maximum positive integer searched] [optional testing mode]`

Run `python main.py` for "input.txt"  
Run `python main.py x x x x` for premade test cases

Parameters:
- File: contains lines with two integers separated by a space where the first integer is an input and the second integer is the corresponding output  
- Maximum search depth (optional): how many times all possible expressions are expanded
- Maximum integer searched (optional): specifies the range of possible values for addition, subtraction, multiplication, and division (by default 10)  
- Testing mode (optional): if anything is specified, runs tests for test files  

Default values:
- File: "inputs.txt"  
- Maximum search depth: 2
- Maximum positive integer searched: 10  
- Testing mode: off unless specified  
