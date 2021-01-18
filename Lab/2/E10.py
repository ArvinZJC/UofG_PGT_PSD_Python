'''
Description: Exercise 10 (random)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 04:40:09
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 10:56:10
'''

import random


computer = random.choice(['h', 't'])
print('You win.' if input('Guess head (h) or tail (t): ').strip().lower() == computer else 'Bad luck.')
print('It was heads.' if computer == 'h' else 'It was tails.')