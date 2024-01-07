"""
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""


class Stack:
    def __init__(self):
        self.items = []

    def input(self, *args):
        for element in args:
            self.items.append(element)

    def __repr__(self):
        representation = ''
        for element in reversed(self.items):
            representation += f'{element}'
        return representation

    def __str__(self):
        return self.__repr__()


"""
Task 2
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
and curly brackets are "balanced."
"""

input_string = input('Enter string: ')
stack = []
flVerify = True

for i in input_string:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and i == ')':
            continue
        if br == '[' and i == ']':
            continue
        if br == '{' and i == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print('Valid')
else:
    print('Invalid')


"""
Task 3
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, *args):
        for i in args:
            self.items.append(i)

    def get_from_stack(self, find_item):
        for index, element in enumerate(reversed(self.items)):
            if element == find_item:
                return f'Element: {element} on index: {index}'
        else:
            raise ValueError('Error')

    def __str__(self):
        return self.__repr__()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, *args):
        for i in args:
            self.items.insert(0, i)

    def get_from_queue(self, find_item):
        for index, element in enumerate(self.items):
            if element == find_item:
                return f'Element: {element} on index: {index}'
        else:
            raise ValueError('Error')

    def __str__(self):
        return self.__repr__()
