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

    def __init__(self, types: str, name: str, price: float):
        self.types = types
        self.name = name
        self.price = price
        self.count = 0

    def __repr__(self):
        return f'{self.types}, {self.name}, {str(self.price)}, {self.count})'


class ProductStore:

    def __init__(self):
        self.list_of_products = []
        self.price_for_store = 30
        self.income = 0

    def add(self, product, amount):
        if amount % 1 != 0:
            raise ValueError('Error')
        elif amount <= 0:
            raise ValueError('Error')
        else:
            product.price *= 1 + (self.price_for_store / 100)
            product.amount = amount
            self.list_of_products.append(product)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product in self.list_of_products:
                if product.name == identifier:
                    product.price -= product.price * (percent/100)
        elif identifier_type == 'type':
            for product in self.list_of_products:
                if product.types == identifier:
                    product.price *= product.price * (percent/100)
        else:
            raise ValueError('No such identifier')

    def sell(self, product_name, amount):
        for product in self.list_of_products:
            if product.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    self.income += amount * product.price
                else:
                    raise ValueError('Error')
        result_list_of_products = [product for product in self.list_of_products if product.amount != 0]
        self.list_of_products = result_list_of_products

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.list_of_products

    def get_product_info(self, product_name):
        for product in self.list_of_products:
            if product.name == product_name:
                return product.name, product.amount


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
        self.error_message = msg.__name__
        self.text_error = msg.__doc__
        self.date_error = datetime.now()
        try:
            raise CustomException('message')
        except:
            with open('../Lesson15/logs.txt', 'a') as file:
                file.write(f'Date error: {self.date_error}\n name error: {self.error_message}\n '
                           f'text error: {self.text_error}\n')
                file.write('#' * 100 + '\n')


assert CustomException(TypeError)
