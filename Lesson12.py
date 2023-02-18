from functools import reduce

"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""


def func():
    """
    This is testing function
    :return:
    """
    a = 'sdfsf'
    bsdfsf = 2323
    t = 85
    ut = 52.25


def count(fun):
    sum_local_var_fun = fun.__code__.co_nlocals
    return sum_local_var_fun

print(count(func))  # output


"""
Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def first_func():
    print('This is first function')


def second_func():
    print('This is second function')
    return first_func


return_func = second_func()

return_func()


"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one
"""


def choose_func(nums: list, func1, func2):
    if all(map(lambda x: x >= 0, nums)):
        return func1(nums)

    return func2(nums)


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
