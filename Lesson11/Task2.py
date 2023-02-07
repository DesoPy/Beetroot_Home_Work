import json
from func_for_task2 import *

"""
Task 2
Extend Phonebook application

Functionality of Phonebook application:

Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
else raise an error. After the user exits, all data should be saved to loaded JSON.
"""

file_name = './Phonebook.json'


while True:
    u_choose = user_choose()
    if u_choose is None:
        pass
    else:
        print(u_choose)
    question_for_user = input('Do you want repeat request [Y/N]?: ')
    if question_for_user.lower() in ['n']:
        print('Program was closed')
        break
    if question_for_user.lower() in ['y']:
        continue
    elif question_for_user is None:
        print('Incorrect input.')
        continue
    elif input('Incorrect input? Do you want repeat request [Y/N]?'):
        continue