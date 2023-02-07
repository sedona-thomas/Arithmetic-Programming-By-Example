# Brute-Force-Programming-By-Example

Determines all valid combinations of addition, subtraction, multiplication, and division within a specified range for given examples.

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

## Assignment 1

Implementation: "arith_expr_brute_force_pbe.py"

The ArithExprBruteForcePBE class uses brute force to find solutions by example for arithmatic expressions the positive integers for addition, multiplication, subtraction, and integer division. Returns all found solutions.

## Assignment 2

Implementation: "arith_expr_bottom_up_pbe.py"

The ArithExprBottomUpPBE class uses a bottom up approach to find solutions by example for arithmatic expressions the positive integers for addition, multiplication, subtraction, and integer division. 

Implements the [bottom up synthesis algorithm](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture3.htm) below
```
Synthesize(inputs, outputs):
    plist := set of all terminals
    while(true):
        plist := grow(plist);
        plist := elimEquvalents(plist, inputs);
    forall( p in plist)
        if(isCorrect(p, inputs, outputs)): return p;
```

Operationally equivalent expressions for the given inputs are eliminated such that the remaining expression has the smallest number of operators.


