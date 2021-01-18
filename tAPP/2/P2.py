'''
Description: Problem 2 (rearrange the code)
Version: 1.0.2.20210118
Author: Arvin Zhao
Date: 2021-01-14 22:35:43
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:11:03
'''

line = input('Enter a string: ')
i = 0
is_palindrome = True

while i < len(line) / 2 and is_palindrome:
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
    else:
        is_palindrome = True

    i += 1

if is_palindrome:
    print(line, 'is a palindrome.')
else:
    print(line, 'is not a palindrome.')