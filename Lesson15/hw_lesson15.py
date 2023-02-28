from datetime import date, datetime

"""
Task 1
School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.
"""


class Person:

    def __init__(self, first_name, last_name, birthday, birthday_city, residence_address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.birthday_city = birthday_city
        self.residence_address = residence_address

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_years(self):
        cnt_full_years = date.today().year - self.birthday.year
        return cnt_full_years


class Student(Person):

    def __init__(self, first_name, last_name, birthday, birthday_city, residence_address,
                 course, scholar, entered_year):
        super().__init__(first_name, last_name, birthday, birthday_city, residence_address)
        self.course = course
        self.scholar = scholar
        self.entered_year = entered_year


class Teacher(Person):

    def __init__(self, first_name, last_name, birthday, birthday_city, residence_address,
                 cathedra, study_field, science_degree):
        super().__init__(first_name, last_name, birthday, birthday_city, residence_address)
        self.cathedra = cathedra
        self.study_field = study_field
        self.science_degree = science_degree


"""
Task 2
Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""


class Mathematician:

    def square_nums(self, some_list: list):
        sqr = list(map(lambda num: num ** 2, some_list))
        return sqr

    def remove_positives(self, some_list: list):
        r_positives = list(filter(lambda num: num < 0, some_list))
        return r_positives

    def filter_leaps(self, some_list: list):
        f_leaps = list(filter(lambda num: num % 4 == 0, some_list))
        return f_leaps


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


"""
Task 3
Product Store

Write a class Product that has three attributes:

type
name
price

Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product
with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:

    c = 0

    def __init__(self, types: str, name: str, price: float):
        self.types = types
        self.name = name
        self.price = price
        self.__class__.c += 1

    def __str__(self):
        return self.types + ', ' + self.name + ', ' + str(self.price)


class ProductStore:

    def __init__(self):
        self.goods = dict()

    def add(self, product, amount):
        self.goods[product.name] = [product.types, product.name, round(product.price * 1.3, 2), amount]
        return tuple(self.goods[product.name])

    def set_discount(self, identifier, percent):
        a = self.goods[identifier]
        a.append(f'{percent} %')
        self.goods.update({self.goods.get(self, identifier): a})
        return self.goods

    def sell(self, product_name, amount):
        a = self.goods[product_name]
        a[3] = a[3] - amount
        self.goods.update({self.goods.get(self, product_name): a})
        return (product_name, self.goods[product_name])

    @staticmethod
    def get_income(cls):
        return cls.c

    def get_all_products(self):
        for i in self.goods.keys():
            return i

    def get_product_info(self, product_name):
        return (product_name, self.goods[product_name][3])

    def __str__(self):
        return str(self.goods)


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)


"""
Task 4
Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file
"""


class CustomException(Exception):

    def __init__(self, msg):
        self.msg = super().__init__()
        error_message = msg.__name__
        text_error = msg.__doc__
        date_error = datetime.now()
        with open('../Lesson15/logs.txt', 'a') as file:
            file.write(f'Date error: {date_error}\n name error: {error_message}\n text error: {text_error}\n')
            file.write('#' * 100 + '\n')


assert CustomException(TypeError)
