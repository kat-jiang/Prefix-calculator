"""CLI application for a prefix-notation calculator."""

from arithmetic import *


while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")

    if "q" in tokens or "quit" in tokens:   # q to quit
        print("You will exit.")
        break

    if len(tokens) < 2:                     # needs minimum of 2 inputs (operator and number)
        print("Not enough inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]
    result = None                           # a place to store the results of the functions

    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    if not num1.isdigit() or not num2.isdigit(): # check to see if digits are after operator
        print("Those aren't numbers!")
        continue
    else:
        num1 = float(num1)                  # converts num1-3 as floats to pass into functions
        num2 = float(num2)
        num3 = float(num3)

        if operator == "+":
            result = add(num1, num2)

        elif operator == "-":
            result = subtract(num1, num2)
        
        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)
            
        elif operator == "square":
            result = square(num1)

        elif operator == "cube":
            result = cube(num1)
        
        elif operator == "pow":
            result = power(num1, num2)        
        
        elif operator == "%":
            result = mod(num1, num2)
        
        elif operator == "x+":
            result = add_mult(num1, num2, num3)

        elif operator == "cubes+":
            result = add_cubes(num1, num2)
        else:
            result = "Please enter an operator followed by two integers."
    
        print(result)
