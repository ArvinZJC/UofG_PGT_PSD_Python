'''
Description: Exercise 25 (numeric array)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 16:08:00
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:14:47
'''

from array import array


num_array = array('f', [10.24, 66.66, 23.33, 99.99, 13.14])

while True:
    num = int(input('Enter a number between 2 and 5: '))

    if num >= 2 and num <= 5:
        break
    else:
        print('Error! Out of the specified range!')

for count in range(5):
    print(round(num_array[count] / num, 2))