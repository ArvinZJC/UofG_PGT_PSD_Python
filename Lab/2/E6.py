'''
Description: Exercise 6 (while loop)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 03:06:13
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 10:46:42
'''

bottle = 10

while bottle > 0:
    answer = int(input('{} {} {} {}'.format(
        bottle,
        'green bottle(s) hanging on the wall,',
        bottle,
        'green bottle(s) hanging on the wall, and if 1 green bottle should accidentally fall, how many green bottles will be hanging on the wall?  ')))
    bottle = bottle - 1

    while answer != bottle:
        answer = int(input('No, try again: '))

    print('{} {} {}'.format('There \'ll be', bottle, 'bottle(s) hanging on the wall.'))
