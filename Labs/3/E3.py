'''
Description: Exercise 3 (file)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 18:20:31
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 20:11:32
'''

import os, sys


file_name = 'Salaries.csv'


def add_to_file() -> None:
    '''
    Add a name and a salary to the file.
    '''

    file = open(file_name, 'a')

    if os.stat(file_name).st_size == 0:
        for header in ['Name', 'Salary']:
            file.write(header + ',')

        file.write('\n\n')

    for content in [input('Enter your name: ').strip(), input('Enter your salary: ').strip()]:
        file.write(content + ',')

    file.write('\n')
    file.close()


def view_records() -> None:
    '''
    View all records.
    '''

    try:
        file = open(file_name, 'r')
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('Error! You need to add to file first.')


def print_error() -> None:
    '''
    Print an error message when the user's choice is invalid.
    '''

    print('Error! No such option!')


if __name__ == '__main__':
    while True:
        print('1) Add to file')
        print('2) View all records')
        print('3) Quit program')
        choice = input('Enter the number of your selection: ').strip()

        operation_switch = {
            '1': add_to_file,
            '2': view_records,
            '3': sys.exit
        }
        operation_switch.get(choice, print_error)()
        print()