'''
Description: Problem 3. Parsons puzzle (rearrange the code)
Version: 1.0.0.20210116
Author: Arvin Zhao
Date: 2021-01-16 00:18:30
Last Editors: Arvin Zhao
LastEditTime: 2021-01-16 04:11:49
'''

import sqlite3
from tkinter import *


def addtolist():
    newname = sname.get()
    newgrade = sgrade.get()
    cursor.execute("""INSERT INTO Scores(name, score) VALUES(?, ?)""", (newname, newgrade))
    db.commit()
    sname.delete(0, END)
    sgrade.delete(0, END)
    sname.focus()


def clearlist():
    sname.delete(0, END)
    sgrade.delete(0, END)
    sname.focus()


if __name__ == '__main__':  # It is strongly recommended to add this line.
    with sqlite3.connect('tAPP/3/TestScore.db') as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
        id integer PRIMARY KEY,
        name text,
        score integer)""")

    window = Tk()
    window.geometry('450x200')
    window.title('TestScores')

    sname = Entry(text = '')
    sname.place(x = 150, y = 35, width = 200, height = 25)
    sname.focus()

    sgrade = Entry(text = '')
    sgrade.place(x = 150, y = 80, width = 200, height = 25)
    sgrade.focus()

    addbtn = Button(text = 'Add', command = addtolist)
    addbtn.place(x = 150, y = 120, width = 75, height = 25)

    clearbtn = Button(text = 'Clear', command = clearlist)
    clearbtn.place(x = 250, y = 120, width = 75, height = 25)

    label1 = Label(text = 'Enter student\'s name:')
    label1.place(x = 30, y = 35)

    label2 = Label(text = 'Enter student\'s grade:')
    label2.place(x = 30, y = 80)

    window.mainloop()