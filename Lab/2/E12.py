'''
Description: Exercise 12 (random)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 04:55:29
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 05:08:57
'''

import random


colour_list = ['green', 'blue', 'red', 'white', 'grey']
computer = random.choice(colour_list)

if input('Guess a colour from ' + str(colour_list) + ': ').strip().lower() == computer:
    print('Well done.')
else:
    colour_hint_switch = {
        'green': 'I bet you are GREEN with envy.',
        'blue': 'You are probably feeling BLUE right now.',
        'red': 'The unfair result is a RED rag to a bull.',
        'white': 'She is really whiter than WHITE.',
        'grey': 'Life seems GREY and pointless without him.'
    }

    while True:
        print(colour_hint_switch.get(computer, 'Error! Cannot find the corresponding hint.'))

        if input('Guess again: ').strip().lower() == computer:
            print('Correct.')
            break