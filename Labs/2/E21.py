'''
Description: Exercise 21 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 15:48:48
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 16:03:20
'''

from array import array
import random


num_array = array('i')

for count in range(5):
    num_array.append(random.randint(1, 50))

for num in num_array:
    print(num)