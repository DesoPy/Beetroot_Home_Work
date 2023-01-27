"""
Task 1
A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.
"""

film_name = str(input('Now, my favorite movie is: '))


def favorite_movie(film_name: str):
    print(f'My favorite movie is named "{film_name}"')


favorite_movie(film_name)

"""
Task 2
Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""

country = str(input('Enter country name: '))
capital = str(input('Enter ts capital: '))


def make_country(country, capital):
    country_capital = {}
    country_capital.update({country: capital})
    return country_capital


print(make_country(country, capital))

"""
Task 3
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""

choice_operation = input('Enter operation (only be ‘+’, ‘-’ or ‘*’): ')
arbitrary_numbers = input('Enter arbitrary numbers (for example 1 2 3): ').split(' ')
arbitrary_numbers = list(arbitrary_numbers)
t_arbitrary_numbers = []

for ii in arbitrary_numbers:
    t_arbitrary_numbers.append(int(ii))

t_arbitrary_numbers = tuple(t_arbitrary_numbers)


def make_operation(choice_operation, *t_arbitrary_numbers):
    if choice_operation == '+':
        plus_result = 0
        for num in t_arbitrary_numbers:
            plus_result += num
        return plus_result
    elif choice_operation == '-':
        minus_result = 0
        for num in t_arbitrary_numbers:
            minus_result -= num
        return minus_result
    elif choice_operation == '*':
        multiplication_result = 1
        for num in t_arbitrary_numbers:
            multiplication_result *= num
        return multiplication_result


print(make_operation(choice_operation, *t_arbitrary_numbers))
