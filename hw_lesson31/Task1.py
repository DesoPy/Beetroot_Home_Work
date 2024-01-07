import concurrent.futures
import multiprocessing
from prime import is_prime

"""
Task 1
Primes

We have the following input list of numbers, some of them are prime. You need to create a utility function
that takes as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.
Compare the results and performance of each of them.
"""


NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


if __name__ == '__main__':
    multiprocessing.freeze_support()

    # ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, NUMBERS)
        print(list(results))

    # ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, NUMBERS)
        print(list(results))
