"""
Task 1

Create your own implementation of a built-in function enumerate, named `with_index`,which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


"""
Task 2

Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


def in_range(start, end, step=1):
    i = start
    if step > 0:
        while i < end:
            yield i
            i += step
        return i
    elif step < 0:
        while i > end:
            yield i
            i += step
        return i


"""
Task 3

Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""


def in_zip(var1, var2):
    iter1 = var1
    iter2 = var2
    while True:
        try:
            yield next(iter1), next(iter2)
        except StopIteration:
            return
