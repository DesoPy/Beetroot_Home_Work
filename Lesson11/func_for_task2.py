import json


def create_phonebook():
    """
    Create new json-file 'phonebook' with first entries
    :param new_entries:
    :return:
    """
    with open('Phonebook.json', 'w') as add_entries:
        new_entries = {'Phonebook': [{'Full name': {'First name': 'John', 'Last name': 'Smith'},
                                      'Phone number': '+380987654321', 'E-mail': 'example@gmail.com', 'City': 'Dnipro'}]}
        json.dump(new_entries, add_entries, indent=4)


def first_name_enter() -> str:
    """
    Function to query 'First name'
    :return:
    """
    enter_first_name = input('Enter first name: ').title()
    return enter_first_name


def last_name_enter() -> str:
    """
    Function to query 'Last name'
    :return:
    """
    enter_last_name = input('Enter last name: ').title()
    return enter_last_name


def phone_number_enter() -> str:
    """
    Function to query 'phone number'
    :return:
    """
    enter_phone_number = input('Enter phone number (12 digits): ')
    return enter_phone_number


def email_enter() -> str:
    """
    Function to query E-mail
    :return:
    """
    enter_email = input('Enter E-mail: ')
    return enter_email


def city_enter() -> str:
    """
    Function to query City
    :return:
    """
    enter_city = input('Enter city: ').title()
    return enter_city


def creat_data_entries() -> dict:
    """
    create dict with data, which was entered user
    :return:
    """
    user_dict = {'Full name': {'First name': ' ', 'Last name': ' '},
                 'Phone number': ' ', 'E-mail': ' ', 'City': ' '}
    user_dict['Full name']['First name'] = first_name_enter()
    user_dict['Full name']['Last name'] = last_name_enter()
    user_dict['Phone number'] = phone_number_enter()
    user_dict['E-mail'] = email_enter()
    user_dict['City'] = city_enter()
    return user_dict


def search_full_name(fn: str, ln: str) -> str:
    """
    fn - enter First name
    ln - enter Last name
    Search entries on 'Full name'
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        ii = 0
        while ii < len(list_data):
            list_j = []
            ii += 1
            for i, j in enumerate(list_data):
                if fn == j['Full name']['First name'] and ln == j['Full name']['Last name']:
                    list_j.append(j)
            return list_j


def search_first_name(fn: str) -> str:
    """
    fn - enter First name
    Search entries on 'First name'
    :param fn:
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        ii = 0
        while ii < len(list_data):
            list_j = []
            ii += 1
            for i, j in enumerate(list_data):
                if fn == j['Full name']['First name']:
                    list_j.append(j)
            return list_j


def search_last_name(ln: str) -> str:
    """
    ln - enter Last name
    Search entries on 'Last name'
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        ii = 0
        while ii < len(list_data):
            list_j = []
            ii += 1
            for i, j in enumerate(list_data):
                if ln == j['Full name']['Last name']:
                    list_j.append(j)
            return list_j


def search_on_phone(ph: str) -> str:
    """
    ph - enter number phone
    Search entries on 'Phone'
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        if len(ph) == 12 and ph.isdigit():
            ii = 0
            while ii < len(list_data):
                list_j = []
                ii += 1
                for i, j in enumerate(list_data):
                    if ph == j['Phone number']:
                        list_j.append(j)
                return list_j
        elif len(ph) < 12:
            output = 'You have entered less than 12 digits'
            return output
        elif len(ph) > 12:
            output = 'You have entered more than 12 digits'
            return output
        else:
            output = 'You haven\'t entered correct number'
        return output


def search_on_City(city: str) -> str:
    """
    city - enter city
    Search entries on 'City'
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        city.strip()
        ii = 0
        while ii < len(list_data):
            list_j = []
            ii += 1
            for i, j in enumerate(list_data):
                if city == j['City']:
                    list_j.append(j)
            return list_j


def del_on_phone(numb: str) -> str:
    """
    Delete a record for a given telephone number
    :param numb: entered telephone number
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        if len(numb) == 12 and numb.isdigit():
            for i, j in enumerate(list_data):
                if numb == j['Phone number']:
                    list_data.remove(j)
                    data['Phonebook'] = list_data
                with open('Phonebook.json', 'w') as file:
                    json.dump(data, file, indent=4)
        elif len(numb) < 12:
            output = 'You have entered less than 12 digits'
            return output
        elif len(numb) > 12:
            output = 'You have entered more than 12 digits'
            return output
        else:
            output = 'You haven\'t entered correct number'
            return output



def update_on_phone(numb: str) -> str:
    """
    Update a record for a given telephone number
    :param numb: entered phone number for search
    :return:
    """
    with open('Phonebook.json', 'r') as file:
        data = json.load(file)
        list_data = data['Phonebook']
        if len(numb) == 12 and numb.isdigit():
            for i, j in enumerate(list_data):
                if numb == j['Phone number']:
                    j['Full name']['First name'] = first_name_enter()
                    j['Full name']['Last name'] = last_name_enter()
                    j['Phone number'] = phone_number_enter()
                    j['E-mail'] = email_enter()
                    j['City'] = city_enter()
                with open('Phonebook.json', 'w') as file:
                    json.dump(data, file, indent=4)
        elif len(numb) < 12:
            output = 'You have entered less than 12 digits'
            return output
        elif len(numb) > 12:
            output = 'You have entered more than 12 digits'
            return output
        else:
            output = 'You haven\'t entered correct number'
            return output


def interface():
    """
    Introductory dialogue
    :return:
    """
    choose = input('Hello, it\'s "Phonebook". You can do next:'
                    '\n1.Add new entries - enter Add'
                    '\n2.Search by first name - enter First name'
                    '\n3.Search by last name - enter Last name'
                    '\n4.Search by full name - enter Full name'
                    '\n5.Search by telephone number - enter Number'
                    '\n6.Search by city or state - enter City'
                    '\n7.Delete a record for a given telephone number - enter Delete'
                    '\n8.Update a record for a given telephone number - enter Update'
                    '\nIf you need exit - enter Exit'
                    '\nWhat do you do? ')
    return choose


def user_choose():
    """
    prints the possible options for the user and accepts the value from the user
    :return:
    """
    while True:
        choose = interface()
        if choose.lower() in ['exit']:
            print('You exit from Phonebook')
            break
        elif choose.lower() == 'first name':
            fn = first_name_enter()
            return_fn = search_first_name(fn)
            return return_fn
        elif choose.lower() == 'last name':
            ln = last_name_enter()
            return_ln = search_last_name(ln)
            return return_ln
        elif choose.lower() == 'full name':
            fn = input('Enter full name: ').split(' ')
            for i in fn:
                fn.remove(' ')
            return_fn = search_full_name(fn[0], fn[1])
            return return_fn
        elif choose.lower() == 'number':
            pn = phone_number_enter()
            return_pn = search_on_phone(pn)
            return return_pn
        elif choose.lower() == 'city':
            city = city_enter()
            return_city = search_on_City(city)
            return return_city
        elif choose.lower() == 'delete':
            pn_del = phone_number_enter()
            return_del_result = del_on_phone(pn_del)
            if return_del_result is None:
                return_del_result = 'User data was delete from Phonebook'
                return return_del_result
            else:
                return return_del_result
        elif choose.lower() == 'update':
            pn_update = phone_number_enter()
            return_up_result = update_on_phone(pn_update)
            if return_up_result is None:
                return_up_result = 'User\'s data was update in Phonebook'
                return return_up_result
            else:
                return return_up_result
        else:
            print('Unsupported command. Try again')
            break
