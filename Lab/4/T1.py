'''
Description: Task 1
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 14:14:20
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 14:21:30
'''

import numpy as np


x = np.array([10, 2, 30, 45])
print('Original array:\n', x)
print('Test if NONE of the elements of the array is 0:\n', np.all(x))