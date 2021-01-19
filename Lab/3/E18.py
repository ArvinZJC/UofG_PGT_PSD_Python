'''
Description: Exercise 18 (SQLite 3)
Version: 1.0.0.20210119
Author: Arvin Zhao
Date: 2021-01-19 18:02:18
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 21:03:02
'''

import sqlite3, sys


database = sqlite3.connect('PhoneBook1.db')
cursor = database.cursor()\


def view() -> None:
    '''
    View the phone book.
    '''

    cursor.execute('SELECT * FROM Names')

    for contact in cursor.fetchall():
        print(contact)


def add() -> None:
    '''
    Add a person to the phone book.
    '''

    first_name = input('Enter the first name: ').strip()
    surname = input('Enter the surname: ').strip()
    phone = input('Enter the phone number: ').strip()
    cursor.execute('INSERT INTO Names (first_name, surname, phone_number) VALUES(?, ?, ?)', (first_name, surname, phone))
    database.commit()


def search() -> None:
    '''
    Search for a surname.
    '''

    surname = input('Enter the surname: ').strip()
    cursor.execute('SELECT * FROM Names WHERE surname = ?', [surname])

    for contact in cursor.fetchall():
        print(contact)


def delete() -> None:
    '''
    Delete a person from the phone book.
    '''

    person_id = int(input('Enter the ID: '))
    cursor.execute('DELETE FROM Names WHERE id = ?', [person_id])
    database.commit()


def quit_program() -> None:
    '''
    Close the database connection and quit the program.
    '''

    database.close()
    sys.exit()


def print_error() -> None:
    '''
    Print an error message when the user's choice is invalid.
    '''

    print('Error! No such option!')


if __name__ == '__main__':
    while True:
        print('1) View phone book')
        print('2) Add to phone book')
        print('3) Search for surname')
        print('4) Delete person from phone book')
        print('5) Quit')
        choice = input('Enter your selection: ').strip()

        operation_switch = {
            '1': view,
            '2': add,
            '3': search,
            '4': delete,
            '5': quit_program
        }
        operation_switch.get(choice, print_error)()
        print()