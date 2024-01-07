import random
from time import time

"""
Task 1

A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.
"""

list_a = []

for x in range(200):
    list_a.append(random.randrange(-50, 50))

for i in range(0, len(list_a) - 1):
    for j in range(0, len(list_a) - 1 - i):
        if list_a[j] > list_a[j + 1]:
            list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

print(f'Result Task 1: {list_a}')


"""
Task 2

Implement the mergeSort function without using the slice operator.
"""


# function to merge two sorted lists
def merge_list(x, y):
    c = []
    N = len(x)
    M = len(y)

    i = 0
    j = 0
    while i < N and j < M:
        if x[i] <= y[j]:
            c.append(x[i])
            i += 1
        else:
            c.append(y[j])
            j += 1

    c += x[i:] + y[j:]
    return c


# function of splitting a list and merging lists into a common sorted list
def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


list_a = split_and_merge_list(list_a)

print(f'Result Task 2: {list_a}')


"""
Task 3

One way to improve the quicksort is to use an insertion sort on lists
that are small in length (call it the “partition limit”).
Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers.
Perform analysis using different list sizes for the partition limit.
"""


list_a = []

for x in range(200):
    list_a.append(random.randrange(-50, 50))


def insertion_sort(value):
    for i in range(1, len(value)):
        ival = value[i]
        ii = i
        while ii > 0 and value[ii - 1] > ival:
            value[ii] = value[ii - 1]
            ii -= 1
        value[ii] = ival
    return value


def quick_sort(value):
    length = len(value)
    if length <= 1:
        return value
    items_greater = []
    items_lower = []
    pivot = value.pop()
    for item in value:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print('Task 3:')
start_time = time()
print(insertion_sort(list_a))
print(f'Different time: {start_time - time()}')
start_time2 = time()
print(quick_sort(list_a))
print(f'Different time: {start_time2 - time()}')
