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
    
    # Validating that inputs are numbers
    try:
        for index, num in enumerate(token_nums):
            key = "num" + str(index + 1)
            value = float(num)
            nums[key] = value
    except:
        print("Don't do that. You know better. Type a number.")
        continue

    # If there were no number inputs
    if nums == {}:
        print("No numbers, no calculations.")
        continue

    # If there's 1 number and there should be two
    if (operator in "+,-,*,/,pow,mod") and (len(nums) == 1):
        print("You want to do that with one number? NO.")
        continue

    # if there's 2 numbers and there should be one
    if (operator in "square,cube") and (len(nums) > 1):
        print("I can only handle one number at a time for that.")
        continue

    num1 = nums['num1']
    num2 = nums['num2']

    result = None

    # Functionality of calculator
    if operator == '+':
        result = (add(num1, num2))

    elif operator == '-':
        result = (subtract(num1, num2))

    elif operator == '*':
        result = (multiply(num1,num2))

    elif operator == '/':
        result = (divide(num1, num2))

    elif operator == 'square':
        result = (square(num1))

    elif operator == 'cube':
        result = (cube(num1))

    elif operator == 'pow':
        result = (power(num1, num2))

    elif operator == 'mod':
        result = (mod(num1, num2))

    else:
        result = "I don't know how to do what you're asking for."

    print(result)


