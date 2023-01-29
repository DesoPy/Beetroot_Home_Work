import os.path
import sys

"""
Task 2
The sys module.

The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python?
If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
"""

filename = 'hw_lesson8'
directory = 'Beetroot_HW'

if not os.path.isdir(directory):
    print(f'Error: directory {directory} does not exist!')
    sys.exit(1)

fullpath = os.path.join(directory, filename)

if not os.path.isdir(fullpath):
    print(f'Error: file {fullpath} does not exist!')
    sys.exit(1)
