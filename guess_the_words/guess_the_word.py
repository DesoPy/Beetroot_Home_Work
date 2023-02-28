from function import *

try:

    player_name = input('For begin enter your name: ').title()

    while True:

        choose_user = hello_choose(player_name)

        choose_loop(choose_user, player_name)

        question_for_user = input('Do you want continue [Y/N]?')

        if question_for_user.lower() not in ['y', ' ']:
            print('Program was closed')
            break
        else:
            continue
except (Exception, SystemExit, KeyboardInterrupt, GeneratorExit):
    print('Oops, something went wrong. Contact support or try again later.,')
