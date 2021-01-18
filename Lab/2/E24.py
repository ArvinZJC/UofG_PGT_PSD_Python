'''
Description: Exercise 24 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 16:02:57
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 16:07:43
'''

from array import array


num_array = array('i', [1, 2, 3, 4, 5])

for num in num_array:
    print(num)

while True:
    num = int(input('Select a number from the array: '))

    if num in num_array:
        print('It is in Position', num_array.index(num))
        break
    else:
        print('Error! It is not a number in the array.')