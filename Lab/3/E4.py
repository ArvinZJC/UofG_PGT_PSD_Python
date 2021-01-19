'''
Description: Exercise 4 (file)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 18:42:23
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 20:31:33
'''

import os, sys, csv


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


def delete_record() -> None:
    '''
    Delete a record from the file.
    '''

    try:
        record_list = list(csv.reader(open(file_name, 'r')))
        name = input('Select a record to delete by entering a name: ').strip()
        has_record = False
        
        for count in range(len(record_list)):
            if len(record_list[count]) != 0 and record_list[count][0] == name:
                has_record = True
                record_list.pop(count)
                break

        if has_record:
            file = open(file_name, 'w')

            for record in record_list:
                if len(record) == 0:
                    file.write('\n')
                else:
                    file.write(record[0] + ',' + record[1] + ',\n')
            
            file.close()
        else:
            print('Error! No such record!')
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
        print('3) Delete a record')
        print('4) Quit program')
        choice = input('Enter the number of your selection: ').strip()

        operation_switch = {
            '1': add_to_file,
            '2': view_records,
            '3': delete_record,
            '4': sys.exit
        }
        operation_switch.get(choice, print_error)()
        print()