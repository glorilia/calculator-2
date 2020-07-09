"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    equation = input("Enter your equation > ")
    tokens = equation.split()

    if 'q' in tokens:
        print("You will exit. No more calculator for you.")
        break

    operator, *token_nums = tokens

    nums = {}
    
    try:
        for num in token_nums:
            num = float(num)
    except:
        print("Don't do that. You know better. Type a number.")
        continue



    num1 = float(token_nums[0])
    if len(token_nums) > 1 :
        num2 = float(token_nums[1])


    result = None

    # Functionality of calculator
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


