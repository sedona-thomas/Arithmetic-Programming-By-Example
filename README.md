# Brute-Force-Programming-By-Example

Determines all valid combinations of addition, subtraction, multiplication, and division within a specified range for given examples. Outputs are in the format `x * a // b + c`. (In order to keep the problem simple and since they could be made into the form `x * a // b + c`, equivalent cases in the form of `(x + a) * b // c` have been ignored.)  

Run for "input.txt" with `python main.py`  

Run with `python main.py [optional file] [optional maximum integer searched] [optional testing mode]`  
Run premade test cases `python main.py x x x`  

Parameters:
- File: contains lines with two integers separated by a space where the first integer is an input and the second integer is the corresponding output  
- Maximum integer searched: specifies the range of possible values for addition, subtraction, multiplication, and division (by default, -10 to 10)  
- Testing mode: if anything is specified, runs tests for test files  

Default values:
- File: "inputs.txt"  
- Maximum integer searched: 10  
- Testing mode: off unless specified  
