"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

def oops():
    raise IndexError


def call_oops():
    try:
        oops()
    except IndexError:
        print('This function catch "IndexError"')


call_oops()

"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b,
construct a try-except block which raises an exception if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).   
"""

def math_func():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    result = (a ** 2) / b
    return result


try:
    math_func()
except ValueError as ve:
    print('You entered not number, try again!')
except ZeroDivisionError as zd:
    print('Second number is zero, cannot divide by zero! Try again.')
