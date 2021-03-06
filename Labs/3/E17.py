'''
Description: Exercise 17 (SQLite3)
Version: 1.0.0.20210119
Author: Arvin Zhao
Date: 2021-01-19 17:38:34
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 20:41:29
'''

import sqlite3


database = sqlite3.connect('PhoneBook1.db')
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Names (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name text,
            surname text,
            phone_number text               
            )''')

cursor.execute('''INSERT INTO Names (first_name, surname, phone_number) VALUES(
    'Simon',
    'Pierre',
    '0142678 9056')''')
cursor.execute('''INSERT INTO Names (first_name, surname, phone_number) VALUES(
    'Katarina',
    'Iglesias',
    '0203456 7078')''')
cursor.execute('''INSERT INTO Names (first_name, surname, phone_number) VALUES(
    'Derrick',
    'Brown',
    '0122345 8765')''')
cursor.execute('''INSERT INTO Names (first_name, surname, phone_number) VALUES(
    'John',
    'Smith',
    '0112653 2312')''')
cursor.execute('''INSERT INTO Names (first_name, surname, phone_number) VALUES(
    'Mark',
    'Isaac',
    '0141657 1383')''')

database.commit()

cursor.execute('SELECT * FROM Names')

for contact in cursor.fetchall():
    print(contact)

database.close()