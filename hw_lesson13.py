from functools import wraps

"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
"""


def logger(func):
    def wrap():

        return func

    return wrap()


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


assert square_all(1, 2, 3) == [1, 4, 9]

assert add(2, 3) == 5


"""
Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    def wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            string: str = func(*args, **kwargs)

            for i in range(len(words)):
                string = string.replace(words[i], '*')

            return string

        return wrapper

    return wrap


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


"""
Task 3

Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def real_decorator(function):
        def wrapped(*args):
            if type(*args) != type_:
                print(f'The parameter type does not match the specified type - "{type_.__name__}"')
                return False
            elif len(*args) > max_length:
                print(f'The length of the passed parameter is longer than {max_length} symbols')
                return False
            elif set(''.join(contains)).issubset(set(args)):
                print(f'The list of characters that the argument must contain must be passed as "{contains}"')
                return False
            return function(*args)
        return wrapped
    return real_decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
