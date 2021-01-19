'''
Description: Exercise 1 (file)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 16:58:49
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 18:21:42
'''

import os


file_name = 'Subjects.txt'


def create_line() -> None:
    '''
    Save a new line to a new file.
    '''

    file = open(file_name, 'w')
    file.write(input('Enter a school subject: ').strip() + '\n')
    file.close()


def display_file() -> None:
    '''
    Display the contents of the file.
    '''

    try:
        file = open(file_name, 'r')
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('Error! You need to create a new line first.')


def add_item() -> None:
    '''
    Append a new item to the file.
    '''

    file = open(file_name, 'a')
    file.write(input('Enter a new subject: ').strip() + '\n')
    file.close()


def print_error() -> None:
    '''
    Print an error message when the user's choice is invalid.
    '''

    print('Error! No such option!')


if __name__ == '__main__':
    print('1) Create a new line')
    print('2) Display the file')
    print('3) Add a new item to the file')
    choice = input('Make a selection to 1, 2, or 3: ').strip()

    operation_switch = {
        '1': create_line,
        '2': display_file,
        '3': add_item
    }
    operation_switch.get(choice, print_error)()