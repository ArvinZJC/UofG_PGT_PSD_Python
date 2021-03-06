'''
Description: Exercise 22 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 15:51:53
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 15:57:43
'''

from array import array
import random


num_array1 = array('i')
num_array2 = array('i')

for count in range(3):
    num_array1.append(int(input('Enter a number: ')))

for count in range(5):
    num_array2.append(random.randint(1, 50))

num_array1.extend(num_array2)

for num in sorted(num_array1):
    print(num)