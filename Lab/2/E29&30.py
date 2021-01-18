'''
Description: Exercises 29 & 30 (2D list and dictionary)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 16:35:36
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 16:52:02
'''

name_dictionary = {}

for count in range(4):
    name = input('Enter your name: ').strip()
    name_dictionary[name] = {'Age': int(input('Enter your age: ')), 'Shoe size': int(input('Enter your shoe size: '))}
    print()

for name in name_dictionary:
    print('Name:', name, ', age:', name_dictionary[name]['Age'])

# Start here for Exercise 30.
print()
name_dictionary.pop(input('Enter the name that you want to remove from the list: ').strip())

for name in name_dictionary:
    print('Name:', name, ', age:', name_dictionary[name]['Age'], ', shoe size:', name_dictionary[name]['Shoe size'])