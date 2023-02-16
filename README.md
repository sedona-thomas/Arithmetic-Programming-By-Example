# Brute-Force-Programming-By-Example

Determines solves for combinations of addition, subtraction, multiplication, and division within a specified range for given examples.

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

"arith_expr_brute_force_pbe.py"

The ArithExprBruteForcePBE class uses brute force to find solutions by example for arithmatic expressions the positive integers for addition, multiplication, subtraction, and integer division

Generates possible solutions recursively by combining all previous possible solutions with each operator

Returns all found solutions within the maximum depth

## Assignment 2

"arith_expr_bottom_up_pbe.py"

The ArithExprBottomUpPBE class uses a bottom up approach to find solutions by example for arithmatic expressions the positive integers for addition, multiplication, subtraction, and integer division. 

Implements the [bottom up synthesis algorithm](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture3.htm) below

```
Synthesize(inputs, outputs):
    operators = "+"
    plist = set(range(max_int)) | {"x"}
    while(true):
        plist = grow(plist)
        plist = elimEquvalents(plist, inputs)
    forall(p in plist):
        if(isCorrect(p, inputs, outputs)): 
            return p

grow(plist):
    forall(operator in operators)
        forall(p1 in plist):
            forall(p2 in plist):
                plist.add(p1 + operator + p2)

elimEquivalents(plist, inputs):
    equivalents = findEquivalents(plist, inputs)
    forall(li in equivalents):
        forall(equivalentExpr in li):
            if equivalentExpr is not minOperators(li):
                plist.remove(equivalentExpr)
```

Repeatedly expands possible solutions and removes all operationally equivalent expressions. The number of operators are minimized as operationally equivalent expressions are removed

Returns the solution at the lowest depth with the smallest number of operators
