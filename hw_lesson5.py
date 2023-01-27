import random

"""
Task 1
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

some_digit = random.randint(1,10)
user_digit = int(input('Please enter integer: '))

while some_digit != user_digit:
    if user_digit < some_digit:
        print('The entered number is less than the specified number')
        user_digit = int(input('Please enter integer: '))
    elif user_digit > some_digit:
        print('Entered is more than less than given')
        user_digit = int(input('Please enter integer: '))
else:
    print(f'Excellent, you guessed the number {some_digit} ')

"""
Task 2
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”    
"""

user_name = input('What is your name?: ')
user_age = int(input('How old are you?'))

print(f'Hello {user_name}, on your next birthday you’ll be {user_age + 1} years')

"""
Task 3
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from
characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
"""

some_word = input('Please enter a word with 5 or more letters: ')

i = 0
new_word1 = ''
new_word2 = ''
new_word3 = ''
new_word4 = ''
new_word5 = ''

if len(some_word) < 5:
    print('Please enter a word with 5 or more letters')
else:
    while i != len (some_word):
        new_word1 = new_word1 + random.choice ( some_word )
        new_word2 = new_word2 + random.choice ( some_word )
        new_word3 = new_word3 + random.choice ( some_word )
        new_word4 = new_word4 + random.choice ( some_word )
        new_word5 = new_word5 + random.choice ( some_word )
        i += 1
    print ('"' + new_word1, new_word2, new_word3, new_word4, new_word5, sep='","', end = '"')

"""
Користувач вводе з клавіатури три цілих числа N, A і B.
Програма шукає всі цілі числа в діапозоні [1 .. N] і виводить:
"Число <number> кратне A!", ящо число діляться на A без залишку;
"Число <number> кратне B!", ящо число діляться на B без залишку.
Якщо число діляться без залишку як на A, так і на B,
програма виводить "Бінго! Число <number> ділеться як на A, так і на B!" і завершує роботу.
"""

n = int(input('Enter first integer number: '))
A = int(input('Enter integer number A: '))
B = int(input('Enter integer number B: '))

i = 0

while i < n:
    i += 1
    if i % A == 0 and i % B == 0:
        print (f'Бінго! Число {i} ділиться як на A, так і на B!')
        break
    elif (i % A) == 0:
        print (f'Число {i} кратне A!')
    elif i % B == 0:
        print (f'Число {i} кратне B!')
