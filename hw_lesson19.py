from unittest import mock
from nose.tools import *
from Lesson11 import func_for_task2

"""
Task 1

Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.
"""

import unittest
from Lesson12 import first_func, second_func


class Task1TestCase(unittest.TestCase):

    def test_Lesson12_first_func(self):
        full = first_func(5)
        self.assertEqual(full, 5)

    def test_Lesson12_second_func(self):
        full1 = first_func(1, 3)
        full2 = second_func()
        self.assertEquals(full1, 4)


if __name__ == '__main__':
    unittest.main()


"""
Task 2

Write tests for the Phonebook application, which you have implemented in module 1.
Design tests for this solution and write tests using unittest library
"""

class TestPhonebookFunction(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_first_name_enter(self):
        func = func_for_task2.first_name_enter
        self.assertTrue(func)

    def test_create_phonebook(self):
        func = func_for_task2.create_phonebook()
        self.assertIsNone(func)

    def test_creat_data_entries(self):
        numb = '12346852585856456454654'
        func = func_for_task2.creat_data_entries(numb)
        self.assertIsNotNone(func)

    def test_search_on_phone(self):
        numb = '12345678'
        func = func_for_task2.search_on_phone(numb)
        self.assertEqual(func, 'You have entered less than 12 digits')

    def test_search_less_on_phone(self):
        numb = '1234567891234564889'
        func = func_for_task2.search_on_phone(numb)
        self.assertEqual(func, 'You have entered more than 12 digits')

    def test_search_more_on_phone(self):
        numb3 = '440123456798'
        func = func_for_task2.search_on_phone(numb3)
        self.assertEqual(func, [])

    def test_del_on_phone(self):
        numb = '123456789123'
        func = func_for_task2.del_on_phone(numb)
        self.assertIsNone(func)

    def test_user_choose(self):
        original_input = mock.builtins.input
        func = func_for_task2.user_choose()
        mock.builtins.input = lambda _: 'Exit'
        assert_equal(func, None)
        mock.builtins.input = original_input


if __name__ == '__main__':
    unittest.main()
