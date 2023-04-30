import math


def is_prime(n):
    if n < 2:
        return 'no prime'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'no prime'
    return 'prime'
