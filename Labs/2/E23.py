'''
Description: Exercise 23 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 15:55:26
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 16:07:30
'''

from array import array


num_array = array('i')

for count in range(5):
    num_array.append(int(input('Enter a number: ')))

num_array = sorted(num_array)

for num in num_array:
    print(num)

num = int(input('Select a number to remove from the array: '))

if num in num_array:
    num_array.remove(num)

    print(num_array)
    print(array('i', [num]))
else:
    print('Error! It is not a number in the array.')