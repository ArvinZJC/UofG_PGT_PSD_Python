'''
Description: Task 2
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 14:21:43
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 14:35:53
'''

import numpy as np


array1 = np.array([45, 67, 23])
array2 = np.array([56, 23, 89])

print('Comparison - greater\n', np.greater(array1, array2))
print('Comparison - greater_equal\n', np.greater_equal(array1, array2))
print('Comparison - less\n', np.less(array1, array2))
print('Comparison - less_equal\n', np.less_equal(array1, array2))