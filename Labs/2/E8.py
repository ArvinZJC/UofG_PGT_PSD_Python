'''
Description: Exercise 8 (function)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 03:34:33
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 04:39:20
'''

import sys


name_list = []


def add_name() -> None:
    '''
    Add a name to the list.
    '''

    name_list.append(input('Enter a name for adding: ').strip())


def change_name() -> None:
    '''
    Change a name in the list.
    '''

    while True:
        num = int(input('Enter the number of the name you want to change (the number starts from 1): '))

        if num > 0 and num <= len(name_list):
            name_list[num - 1] = input('Enter a name for changing: ').strip()
            break
        else:
            print('Error! Invalid number.')


def delete_name() -> None:
    '''
    Delete a name from the list.
    '''

    while True:
        num = int(input('Enter the number of the name you want to delete (the number starts from 1): '))

        if num > 0 and num <= len(name_list):
            name_list.remove(name_list[num - 1])
            break
        else:
            print('Error! Invalid number.')


def view_name() -> None:
    '''
    View all the names in the list.
    '''

    print(name_list)


def print_error() -> None:
    '''
    Print an error message when the user's choice is invalid.
    '''

    print('Error! No such option.')


if __name__ == '__main__':
    while True:
        print('1) Add a name to the list')
        print('2) Change a name in the list')
        print('3) Delete a name from the list')
        print('4) View all the names in the list')
        print('5) Quit')

        choice = input('Select an option: ').strip()

        choice_switch = {
            '1': add_name,
            '2': change_name,
            '3': delete_name,
            '4': view_name,
            '5': sys.exit
        }
        choice_switch.get(choice, print_error)()
        print()