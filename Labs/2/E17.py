'''
Description: Exercise 17 (list)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 11:17:44
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 11:33:57
'''

party = [
    input('Enter the first name: ').strip(),
    input('Enter the second name: ').strip(),
    input('Enter the third name: ').strip()]

while True:
    if input('Do you want to add another? (y/n)  ').strip().lower() == 'y':
        party.append(input('Enter another name: ').strip())
    else:
        print('You have', len(party), 'people invited to the party.')
        break