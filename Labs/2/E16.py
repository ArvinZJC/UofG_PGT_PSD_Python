'''
Description: Exercise 16 (list)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 05:46:19
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 11:17:32
'''

num_list = [123, 345, 234, 765]

for num in num_list:
    print(num)

choice = int(input('Enter a number from the list: '))
print(choice, 'is in Position', num_list.index(choice) if choice in num_list else 'It is not in the list.')