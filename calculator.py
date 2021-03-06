"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce


while True:
    equation = input("Enter your equation > ")
    tokens = equation.split()

    if 'q' in tokens:
        print("You will exit. No more calculator for you.")
        break

    operator, *token_nums = tokens

    nums = []
    
    # Validating that inputs are numbers
    try:
        for num in token_nums:
            nums.append(float(num))
    except:
        print("Don't do that. You know better. Type a number.")
        continue

    # If there were no number inputs
    if len(nums) == 0:
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

    result = None

    # Functionality of calculator
    if operator == '+':
        result = reduce(add, nums)

    elif operator == '-':
        result = reduce(subtract, nums)

    elif operator == '*':
        result = reduce(multiply, nums)

    elif operator == '/':
        result = reduce(divide, nums)

    elif operator == 'square':
        result = square(nums[0])

    elif operator == 'cube':
        result = cube(nums[0])

    elif operator == 'pow':
        result = reduce(power, nums)

    elif operator == 'mod':
        result = reduce(mod, nums)

    else:
        result = "I don't know how to do what you're asking for."

    print(result)


