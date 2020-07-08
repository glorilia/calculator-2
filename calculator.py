"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    equation = input("Enter your equation > ")
    tokens = equation.split()
    if tokens[0] == 'q':
        print("You will exit.")
        break

