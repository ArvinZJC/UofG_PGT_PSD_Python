'''
Description: exercise: upper or lower case name
Version: 1.0.1.20210117
Author: Arvin Zhao
Date: 2021-01-13 06:54:05
Last Editors: Arvin Zhao
LastEditTime: 2021-01-17 12:11:25
'''

while True:
    first = input('Enter your first name: ').strip()
    first_len = len(first)  # The length of the input for the first name.

    if first_len == 0:
        print('Please do enter something!')
    else:
        if first_len < 5:
            while True:
                last = input('Enter your last name: ')

                if len(last) == 0:
                    print('Please do enter something')
                else:
                    print(first.upper() + last.upper())
                    break
        else:
            print(first.lower())

        break