"""
Task 1
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different.
For instance, Dog’s can be to print ‘woof, woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Animal can\'t speak')

    def __str__(self):
        return f'{self.name} says {self.talk()}'


class Dog(Animal):

    def talk(self):
        return 'woof, woof'


class Cat(Animal):

    def talk(self):
        return 'meow'


"""
Task 2
Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class
and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""


class Author:

    def __init__(self, name, country, birthday, books=None):
        if books is None:
            books = []
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f'Author: {self.name}'

    def __str__(self):
        return f'{self.name} has {self.books}. Author country - {self.country}'


class Book:
    count_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.count_books += 1

    def __repr__(self):
        return f'Book: {self.name}'

    def __str__(self):
        return f'{self.name} was written in {self.year} by {self.author}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return f'Library "{self.name}" consist with {len(self.books)} books'

    def new_book(self, name, year, author):
        """ returns an instance of Book class and adds the book to the books list for the current library"""
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book.name)
        self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        """ returns a list of all books grouped by the specified author"""
        return [book for book in self.books if book.author is author]

    def group_by_year(self, year: int) -> list:
        """ returns a list of all the books grouped by the specified year"""
        return [book for book in self.books if book.year == year]


"""
Task 3
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
з належною перевіркою й обробкою помилок.
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
"""


class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Error')

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if str(other).find('/') == -1:
            other = Fraction(other)
        n = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __sub__(self, other):
        if str(other).find('/') == -1:
            other = Fraction(other)
        n = (self.numerator * other.denominator) + (self.denominator * -1 * other.numerator)
        d = (self.denominator * other.denominator)
        result = Fraction(n, d)
        result.simplify()
        return result

    def __mul__(self, other):
        if str(other).find('/') == -1:
            other = Fraction(other)
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        if str(other).find('/') == -1:
            other = Fraction(other)
        result = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        result.simplify()
        return result

    def __pow__(self, power):
        if str(power).find('/') == -1:
            power = Fraction(power)
        result = Fraction(self.numerator ** power.digits(), self.denominator ** power.digits())
        result.simplify()
        return result

    def simplify(self):
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator /= a
        self.denominator /= a

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    var = x + y == Fraction(3, 4)
