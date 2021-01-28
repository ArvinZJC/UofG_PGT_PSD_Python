'''
Description: Task 6
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 14:47:26
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 14:50:57
'''

import numpy as np


array1 = np.array([23, 45, 11, 5])
array2 = np.array([23, 5,1])

print('Array1\n', array1)
print('Array2\n', array2)
print('Common values between 2 arrays\n', np.intersect1d(array1, array2))