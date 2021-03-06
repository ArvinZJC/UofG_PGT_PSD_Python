'''
Description: Exercise 28 (2D list and dictionary)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 16:28:31
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 16:35:16
'''

num_list = [
    [2, 5, 8],
    [3, 7, 4],
    [1, 6, 9],
    [4, 2, 0]]
row = int(input('Select a row (start from 0): '))

print(num_list[row])

column = int(input('Select a column (start from 0): '))

print(num_list[row][column])

if input('Do you want to change the value? (y/n)  ').strip().lower() == 'y':
    num_list[row][column] = int(input('Enter a new value: '))

print(num_list[row])