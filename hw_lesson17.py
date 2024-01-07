import re
from functools import wraps

"""
Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
"""


class Validate:

    def __init__(self, validate_email: str):
        if not isinstance(validate_email, str):
            raise TypeError('Error type email!!!')

        if not re.match('\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', validate_email):
            raise TypeError('Error type email!!!')

        self.validate_email = validate_email


"""
Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def boss(self):
        return self.id, self.name, self.company, self.workers

    @boss.setter
    def boss(self, workers):
        self.workers.append(workers)

    def __repr__(self):
        return self.name


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def worker(self):
        return self.id, self.name, self.company, self.boss

    @worker.setter
    def worker(self, boss):
        self.boss = boss

    def __repr__(self):
        return self.name


"""
Task 3
Write a class TypeDecorators which has several methods for converting results of functions
to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float
"""


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def inner(*args):
            try:
                return int(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_str(func):
        @wraps(func)
        def inner(*args):
            try:
                return str(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def inner(*args):
            try:
                return bool(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner

    @staticmethod
    def to_float(func):
        @wraps(func)
        def inner(*args):
            try:
                return float(func(*args))
            except Exception as e:
                print(e.__class__, e)
                return None

        return inner


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
