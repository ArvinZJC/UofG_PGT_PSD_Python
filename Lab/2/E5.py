'''
Description: Exercise 5 (while loop)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 02:56:03
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 03:05:20
'''

compnum = 50
count = 0

while True:
    guess = int(input('Guess the number: '))
    count = count + 1

    if guess == compnum:
        print('{} {} {}'.format('Well done, you took', count, 'attempts.'))
        break
    else:
        print('Your guess is too high.' if guess > compnum else 'Your guess is too low.')