import json
import string
import random
import datetime
from typing import Optional


def create_list():
    with open('words.txt', 'r') as file:
        list_words = file.readlines()
        for posit, word in enumerate(list_words):
            list_words[posit] = word.strip().lower()
    return list_words


def rules_for_user():
    with open('Rules.txt', 'r') as file:
        open_file = file.read()
    return open_file


def hello_choose(player_name: str) -> str:
    choose_eser = input(f'Hello, {player_name}. Choose what you need:'
                        f'\n1. Read rules of game - type "rules"'
                        f'\n2. To start game - type "start"'
                        f'\n3. To stop game - type "stop"'
                        f'\n4. Show past result - type "result"')
    return choose_eser


def search_result(name_player: str) -> str:
    with open('guess_result.json', 'r') as file:
        data = json.load(file)
        list_data = data['Result of games']
        ii = 0
        while ii < len(list_data):
            list_j = []
            ii += 1
            for i, j in enumerate(list_data):
                if name_player == j['Player name']:
                    list_j.append(j)
            return list_j


def choose_loop(choose_user: str, player_name: str) -> str:
    if choose_user == 'rules'.lower():
        rules = rules_for_user()
        print(rules)
    elif choose_user == 'stop'.lower():
        print('Game was stopped')
    elif choose_user == 'start'.lower():
        body_loop(player_name)
    elif choose_user == 'result'.lower():
        name_player = input('Enter player name: ').title()
        result_search = search_result(name_player)
        if not len(result_search):
            print('Player not defined. Try another name!')
        else:
            print(result_search)

    else:
        print('Incorrect input.')


def result_add(count_dict):
    with open('guess_result.json', 'r') as file:
        data = json.load(file)
        list_data = data['Result of games']
        add_list = count_dict
        list_data.append(add_list)
    with open('guess_result.json', 'w') as file:
        json.dump(data, file, indent=4)


def body_loop(player_name):
    count_dict = {'Date time game': '', 'Player name': player_name, 'Game result': 'Lose',
                  'Score': {'Count tries': 0, 'Score points': 0}}

    target_word = random.choice(create_list())

    i = 0
    while i < 6:
        player_letters = list(input(f'Attempt {i + 1} of 6: ').lower())

        if set(player_letters) - set(string.ascii_lowercase):
            print("Unsupported symbols, use letters instead")
            continue

        if len(player_letters) > 5:
            print('You enter word more then 5 letters')
            continue
        elif len(player_letters) < 5:
            print('You enter word less then 5 letters')
            continue

        target_letters = list(target_word)

        for position, letter in enumerate(player_letters):
            if letter == target_letters[position]:
                player_letters[position] = '!'
                target_letters[position] = None  # Mark as "found"

        target_letters = [i for i in target_letters if i]

        for position, letter in enumerate(player_letters):
            if letter == '!':
                continue

            if letter in target_letters:
                player_letters[position] = '?'
                target_letters.remove(letter)
            else:
                player_letters[position] = '.'

        count_dict['Score']['Score points'] = count_dict['Score']['Score points'] \
                                              + (player_letters.count('!') * 0.5) + (player_letters.count('?') * 0.25)
        count_dict['Score']['Count tries'] = 1 + i

        print(player_letters)

        if player_letters == ['!'] * 5:
            count_dict['Game result'] = 'Won'
            count_dict['Date time game'] = str(datetime.datetime.now())
            if i == 0:
                count_dict['Score']['Score points'] = 100
                print(f'Congrats, you\'ve won.The guessed word is "{target_word}" '
                      f'and your score result is {count_dict["Score"]["Score points"]} points')
                result_add(count_dict)
            else:
                count_dict['Score']['Score points'] = count_dict['Score']['Score points'] + (97.5 - (i * 10))
                count_dict['Date time game'] = str(datetime.datetime.now())
                print(f'Congrats, you\'ve won.The guessed word is "{target_word}" '
                      f'and your score result is {count_dict["Score"]["Score points"]} points')
                result_add(count_dict)
            break

        i += 1

    else:
        count_dict['Date time game'] = str(datetime.datetime.now())
        print(f'Sorry, you didn\'t guess the word. '
              f'The guessed word is "{target_word}" and your score result'
              f' is {count_dict["Score"]["Score points"]} points')
        result_add(count_dict)
