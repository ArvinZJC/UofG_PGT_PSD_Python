'''
Description: Exercise 5 (sum a collection of numbers)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 20:32:36
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 20:38:52
'''

total = 0

while True:
    num = input('Enter a number: ')

    try:
        num = float(num)
        total += num
    except ValueError:
        if num.strip() == '':
            break
        else:
            print('Error! Avoid non-numeric input!')

print('Total:', total)