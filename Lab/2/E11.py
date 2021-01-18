'''
Description: Exercise 11 (random)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 04:47:06
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 04:47:06
'''

import random


computer = random.randint(1, 5)
user = int(input('Guess from 1 to 5: '))

if user == computer:
    print('Well done')
else:
    print('Your guess is too high.' if user > computer else 'Your guess is too low.')
    print('Correct' if int(input('Guess again: ')) == computer else 'You lose.')