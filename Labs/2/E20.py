'''
Description: Exercise 20 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 13:44:08
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 15:48:35
'''

from array import array


num_array = array('i')

for count in range(5):
    num = int(input('Enter a number: '))
    num_array.append(num)

num_array = sorted(num_array)
num_array.reverse()
print(num_array)