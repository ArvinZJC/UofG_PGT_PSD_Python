'''
Description: Task 7
Version: 1.0.0.20210128
Author: Arvin Zhao
Date: 2021-01-28 15:44:12
Last Editors: Arvin Zhao
LastEditTime: 2021-01-28 15:49:21
'''

import numpy as np


array1 = np.array([
    [23, 45, 11],
    [12, 23, 54],
    [1, 23, 10]
])
array2 = np.array([
    [3, 5, 1],
    [2, 3, 4],
    [9, 1, 4]])

print('The two arrays stacked horizontally')
print(np.hstack((array1,array2)))

print('The two arrays stacked vertically')
print(np.vstack((array1,array2)))

print('Split array 1 horizontally:\n')
for i in np.hsplit(array1,3):
    print('Splitted here: \n', i)
    
print('Split array 2 horizontally:\n')
for i in np.hsplit(array2,3):
    print('Splitted here: \n', i)
    
print('Split array 1 vertically:\n')

for i in np.vsplit(array1,3):
    print('Splitted here: \n', i)

print('Split array 2 vertically:\n')

for i in np.vsplit(array2,3):
    print('Splitted here: \n', i)