"""
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком
"""


# binary search O(nlogn)
def binary_search(item, seq):
    if len(seq) == 0:
        return False
    mid = len(seq) // 2
    if seq[mid] == item:
        return True
    elif item < seq[mid]:
        return binary_search(item, seq[:mid])
    elif item > seq[mid]:
        return binary_search(item, seq[mid+1:])


# fibonacci search O(n)
def fibonacci_search(item, seq):
    fib_min_2 = 0
    fib_min_1 = 1
    fib = fib_min_1 + fib_min_2
    while fib < len(seq):
        fib_min_2 = fib_min_1
        fib_min_1 = fib
        fib = fib_min_1 + fib_min_2
    index = -1
    while fib > 1:
        i = min(index + fib_min_2, len(seq) - 1)
        if seq[i] < item:
            fib = fib_min_1
            fib_min_1 = fib_min_2
            fib_min_2 = fib - fib_min_1
            index = i
        elif seq[i] > item:
            fib = fib_min_2
            fib_min_1 = fib_min_1 - fib_min_2
            fib_min_2 = fib - fib_min_1
        else:
            return i
    if fib_min_1 and index < (len(seq) - 1) and seq[index + 1] == item:
        return index + 1
    return -1
