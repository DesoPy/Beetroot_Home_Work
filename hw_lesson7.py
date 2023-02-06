"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values.
"""

a = input('Enter sentence (a string): ')
b = a.split(' ')
d = {}

for i in b:
    d[i] = b.count(i)

print(d)

"""
Task 2

Compute the total price of the stock where the total price is the sum of the price of an item
multiplied by the quantity of this exact item.
"""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = stock.copy()

for key, value in total_price.items():
    a = total_price[key] * prices[key]
    total_price[key] = a
print(total_price)

"""
Task 3
List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j)
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""


u_list = []

for i in range(1, 11):
    a_tuple = (i, i * i)
    u_list.append(a_tuple)
print(u_list)

"""
Task 4

Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""


day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_one = {}
dict_two = {}

for i in range(1, 8):
    dict_one.update({i: day_list[i - 1]})
print(dict_one)

for i in range(1, 8):
    dict_two.update({day_list[i - 1]: i})
print(dict_two)
