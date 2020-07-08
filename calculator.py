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

    num1 = float(tokens[1])
    if len(tokens) > 2 :
        num2 = float(tokens[2])

    if operator == '+':
        print(add(num1, num2))
    if operator == '-':
        print(subtract(num1, num2))
    if operator == '*':
        print(multiply(num1,num2))
    if operator == '/':
        print(divide(num1, num2))
    if operator == 'square':
        print(square(num1))
    if operator == 'cube':
        print(cube(num1))
    if operator == 'pow':
        print(power(num1, num2))
    if operator == 'mod':
        print(mod(num1, num2))


