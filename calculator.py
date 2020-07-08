"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    equation = input("Enter your equation > ")
    tokens = equation.split()
    operator = tokens[0]
    if operator == 'q':
        print("You will exit.")
        break

    result = None

    num1 = float(tokens[1])
    if len(tokens) > 2 :
        num2 = float(tokens[2])

    if operator == '+':
        result = (add(num1, num2))

    if operator == '-':
        result = (subtract(num1, num2))

    if operator == '*':
        result = (multiply(num1,num2))

    if operator == '/':
        result = (divide(num1, num2))

    if operator == 'square':
        result = (square(num1))

    if operator == 'cube':
        result = (cube(num1))

    if operator == 'pow':
        result = (power(num1, num2))

    if operator == 'mod':
        result = (mod(num1, num2))

    print(result)


