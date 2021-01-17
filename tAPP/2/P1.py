'''
Description: Problem 1 (rearrange the code)
Version: 1.0.1.20210117
Author: Arvin Zhao
Date: 2021-01-14 22:27:22
Last Editors: Arvin Zhao
LastEditTime: 2021-01-17 12:12:47
'''

message = input('Enter a message (blank to quit): ')

while message != '':
    n = int(input('How many times should it be repeated?'))

    for i in range(n):
        print(message)

    message = input('Enter a message (blank to quit): ')