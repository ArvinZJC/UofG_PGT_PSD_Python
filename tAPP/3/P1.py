'''
Description: Problem 1
Version: 1.0.0.20210116
Author: Arvin Zhao
Date: 2021-01-16 00:07:36
Last Editors: Arvin Zhao
LastEditTime: 2021-01-16 03:53:57
'''

import sqlite3


database = sqlite3.connect('tAPP/3/employees.db')  # Connect to the specified database (create one if there is none).
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contactDetails(
    age integer,
    first text,
    surname text,
    telephone text)""")  # Create a specified table.

# Insert data into the table.
cursor.execute("""INSERT INTO contactDetails(age, first, surname, telephone) VALUES(
    42,
    'Derrick',
    'Brown',
    '0122345 8765')""")
cursor.execute("""INSERT INTO contactDetails(age, first, surname, telephone) VALUES(
    62,
    'Simon',
    'Pierre',
    '0142678 9056')""")
cursor.execute("""INSERT INTO contactDetails(age, first, surname, telephone) VALUES(
    72,
    'Katarina',
    'Iglesias',
    '0203456 7078')""")
database.commit()  # Save changes.

cursor.execute("SELECT * FROM contactDetails")

for contact in cursor.fetchall():
    print(contact)

database.close()  # It is important to close the database when necessary.