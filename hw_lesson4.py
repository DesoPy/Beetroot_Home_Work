import random  # for the task 3

"""
Task 1
String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: 'x'
Expected Result: Empty String
Tips:
Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""

a = input('Enter text: ')

if len(a) >= 2:
    b = a[:2]
    c = a[-2:]
    print(b + c)
else:
    print('Empty String')

"""
Task 2
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

a = input('Enter phone number: ')

if a.isdigit():
    if len(a) == 10:
        print('Your number phone is valid')
    elif len(a) < 10:
        print('You miss some digits')
    elif len(a) > 10:
        print('You have entered more digits')
else:
    print('You must enter a 10 digits phone number')

"""
Task 3
The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.
"""

questions = ({'2 + 2 = ?': float(2 + 2),
              '4 * 4 = ?': float(4 * 4),
              '111 / 8 = ?': float(111 / 8)})
str_for_random = list(questions.keys())
get_question = random.choice(str_for_random)

print(f'Give the correct answer to the question(only digit): {get_question}')
answer = float(input('Your answer: '))

search_key = questions.get(get_question)

if float(answer) == search_key:
    print('You win!!!')
else:
    print('Not true. Try again')

"""
Task 4
The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

my_name = 'serhii'

a = input('What is your name?: ')

if a.lower() == my_name:
    print(f'I know you, you are {my_name}')
else:
    print(f'You are not {my_name}, you are {a}')

"""
Task from lecture

Дана змінна month, яка може приймати будь-яке значення.
Необхідно написати програму, яка виведе строку "Ви народились <сезон>", в залежності від номеру місяця.
Програма повинна починатися з рядка:
month = ...  # Any value
"""

month = input('Enter month: ')

if month.lower() in ('december', 'january', 'february'):
    print('Now is Winter')
elif month.lower() in ('march', 'april', 'may'):
    print('Now is Spring')
elif month.lower() in ('june', 'july', 'august'):
    print('Now is Summer')
elif month.lower() in ('september', 'october', 'november'):
    print('Now is Autumn')
else:
    print('You entered the wrong month name, please try again.')
