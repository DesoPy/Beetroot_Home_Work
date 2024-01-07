import logging
import unittest
"""
Task 1
File Context Manager class

Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method
"""


class LikeOpen:
    _cnt = 0

    def __init__(self, file_name, method):
        LikeOpen._cnt += 1
        logging.basicConfig(filename='logs.log', level=logging.INFO)
        self.file_object = open(file_name, method, encoding=None)

    def __enter__(self):
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()


"""
Task 2
Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it.
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you have errors in the runtime context suite.
"""


class TestingLikeOpen(unittest.TestCase):

    def test_open(self):
        with LikeOpen('my_test.txt', 'w+') as f:
            self.assertTrue(f, True)

    def test_close(self):
        with LikeOpen('my_test.txt', 'r+') as f:
            f.read()
        self.assertTrue(f.closed, True)

    def test_not_close(self):
        with LikeOpen('my_test.txt', 'r+') as f:
            f.read()
            self.assertFalse(f.closed, False)

    def test_mod(self):
        with LikeOpen('my_test.txt', 'o') as f:
            f.read()
            self.assertFalse(f.closed, False)


if __name__ == '__main__':
    unittest.main()
