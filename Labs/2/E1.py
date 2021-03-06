'''
Description: Exercise 1 (for loop)
Version: 1.0.0.20210117
Author: Arvin Zhao
Date: 2021-01-17 17:04:38
Last Editors: Arvin Zhao
LastEditTime: 2021-01-17 18:02:19
'''

name = input('Enter your name: ').strip()
num = int(input('Enter a number: '))

if num < 10:
    for count in range(num):
        print(name)
else:
    for count in range(3):
        print('Too high.')