'''
Description: Task 4
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 14:39:05
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 14:43:46
'''

import numpy as np


m = np.array([
    [23, 45, 11],
    [12, 23, 54],
    [29, 19, 34],
    [1, 23, 10]
])
v = np.array([2, 0, 2])

print('Original matrix\n', m)
print('Original vector\n', v)
print('After adding the vector v to each row of the matrix m\n', m + v)