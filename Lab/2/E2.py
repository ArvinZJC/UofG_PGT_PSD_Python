'''
Description: Exercise 2 (for loop)
Version: 1.0.0.20210117
Author: Arvin Zhao
Date: 2021-01-17 17:38:06
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:01:27
'''

total = 0

for count in range(5):
    num = int(input('Enter a number: '))
    is_included = input('Do you want this number to be included? (y/n)  ').strip().lower()

    if is_included == 'y':
        total += num

print('Total:', total)