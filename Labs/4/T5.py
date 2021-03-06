'''
Description: Task 5
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 14:45:12
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 14:47:17
'''

import numpy as np


x = np.ones((5, 5))
x[1:-1, 1:-1] = 25

print(x)
