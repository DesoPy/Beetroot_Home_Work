import random

"""
Task 1
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""

i = 0
my_random_list = []

while i < 10:
    numb = random.randint(0, 1000)
    my_random_list.append(numb)
    i += 1

print(my_random_list)
print(max(my_random_list))

"""
Task 2
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""

i = 0
my_random_list1 = []
my_random_list2 = []

while i < 10:
    numb = random.randint(0, 10)
    my_random_list1.append(numb)
    numb = random.randint(0, 10)
    my_random_list2.append(numb)
    i += 1

my_random_list3 = set(my_random_list1).intersection(set(my_random_list2))

print(my_random_list3)

"""
Task 3
Extracting numbers.

Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7 but not a multiple of 5,
and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""

my_list_task3 = list(range(1, 101))
final_list = []
i = 0

while i < len(my_list_task3):
    if float(my_list_task3[i]) % 7 == 0 and float(my_list_task3[i]) % 5 != 0:
        numb3 = my_list_task3[i]
        final_list.append(numb3)
    i += 1

print(final_list)