"""
Task 1
The greeting program.
Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
"Good day <name>! <day> is a perfect day to learn some python."

Note that  <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods for constructing result string.
"""

name = 'Serhii'
date = '15.01.2023'

print(f'Good day, {name}! {date} is a perfect day to learn some python.')
print('Good day, {}! {} is a perfect day to learn some python.'.format(name, date))
print('Good day, %s! %s is a perfect day to learn some python.' % (name, date))

"""
Task 2
Manipulate strings.
Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
"""

first_name = 'Serhii'
last_name = 'Hlotov'

print(first_name + ' ' + last_name)

"""
Task 3
Using python as a calculator.
Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 
Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

a = 55
b = 15

print(a + b)  #Addition
print(a - b)  #Subtraction
#Division
print(a / b)
print(b / a)
print(a * b) #Multiplication

#Exponent (Power)
print(a ** b)
print(b ** a)

#Modulus
print(abs(a))
print(abs(b))
print(abs(a - b))
print(abs(b - a))

#Floor division
print(a // b)
print(b // a)
