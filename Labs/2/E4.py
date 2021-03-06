'''
Description: Exercise 4 (while loop)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 02:45:02
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:08:18
'''

total = int(input('Enter a number: '))

while True:
    num = int(input('Enter another number: '))
    total += num
    choice = input('Do you want to add another number? (y/n)  ').strip().lower()

    if choice != 'y':
        break

print('Total:', total)