"""
Task 1

Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def append(self, item):
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self.head
        while current is not None:
            temp_list.add(current.get_data())
            current = current.get_next()
        temp_list.add(item)
        current = temp_list.head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def index(self, num):
        i = 0
        current = self.head
        while current is not None:
            if i == num:
                return current.get_data()
            else:
                i += 1
                current = current.get_next()
        else:
            return 'Error'

    def pop(self):
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self.head
        while current is not None:
            temp_list.add(current.get_data())
            current = current.get_next()
        current = temp_list.head
        i = 0
        while current is not None:
            if i == 0:
                result = current.get_data()
                current = current.get_next()
                i = 1
            new_list.add(current.get_data())
            current = current.get_next()
        return result, new_list

    def insert(self, num, item):
        i = 0
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self.head

        while current is not None:
            if i == num:
                temp_list.add(item)
            temp_list.add(current.get_data())
            current = current.get_next()
            i += 1
        current = temp_list.head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def slice_stack(self, start, stop):
        i = 0
        temp_list = UnorderedList()
        new_list = UnorderedList()
        current = self.head
        while current is not None:
            if start <= i < stop:
                temp_list.add(current.get_data())
                current = current.get_next()
                i += 1
            else:
                current = current.get_next()
                i += 1
        current = temp_list.head
        while current is not None:
            new_list.add(current.get_data())
            current = current.get_next()
        return new_list

    def __repr__(self):
        representation = ''
        current = self.head
        while current is not None:
            representation += str(current.get_data()) + ' '
            current = current.get_next()
        return representation

    def __str__(self):
        return self.__repr__()


"""
Task 2

Implement a stack using a singly linked list.
"""


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        current = self.head
        self.head = self.head.next_node
        return current.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def __repr__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data) + ' '
            current = current.next_node
        return res


"""
Task 3

Implement a queue using a singly linked list.
"""


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def dequeue(self):
        current = self.head
        previous = None
        while current.next_node:
            previous = current
            current = current.next_node
        if previous:
            previous.next_node = None
        else:
            self.head = None
        return current.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def __repr__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data) + ' '
            current = current.next_node
        return res
