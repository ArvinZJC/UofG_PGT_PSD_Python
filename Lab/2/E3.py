'''
Description: Exercise 3 (for loop)
Version: 1.0.0.20210117
Author: Arvin Zhao
Date: 2021-01-17 17:46:34
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 10:40:04
'''

direction = input('Which direction do you want to count? (up/down)').strip().lower()

if direction == 'up':
    top = int(input('Enter the top number: '))

    for count in range(top):
        print(count + 1)
elif direction == 'down':
    bottom = int(input('Enter a number below 20: '))

    for count in range(20, bottom - 1, -1):
        print(count)
else:
    print('I don\'t understand.')