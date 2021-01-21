'''
Description: Problem 2. Debugging code (correct errors)
Version: 1.0.3.20210121
Author: Arvin Zhao
Date: 2021-01-16 00:09:06
Last Editors: Arvin Zhao
LastEditTime: 2021-01-21 16:11:42
'''

#  Using star imports is not wrong but is not recommended.
from tkinter import Tk, Label, Entry, Button
from tkinter.constants import END


def create_new():
    file = open('ages.csv', 'w')  # ".cvs" is wrong.
    file.close()


def save_list():
    file = open('ages.csv', 'a')  # "w" mode is wrong.
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ',' + age + '\n'  # Some strings are wrong.
    file.write(newrecord)  # "srt()" is wrong.
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()


if __name__ == '__main__':  # It is strongly recommended to add this line.
    window = Tk()
    window.title('People List')
    window.geometry('400x100')

    label1 = Label(text = 'Enter a name:')
    label1.place(x = 20, y = 20, width = 100, height = 25)

    name_box = Entry(text = '')
    name_box.place(x = 120, y = 20, width = 100, height = 25)
    name_box['justify'] = 'left'  # Lack the left square bracket.
    name_box.focus()

    label2 = Label(text = 'Enter their age:')
    label2.place(x = 20, y = 50, width = 100, height = 25)

    age_box = Entry(text = '')
    age_box.place(x = 120, y = 50, width = 100, height = 25)  # Redundant right bracket.
    age_box['justify'] = 'left'

    button1 = Button(text = 'Create new file', command = create_new)
    button1.place(x = 250, y = 20, width = 100, height = 25)  # Miss a dot.

    button2 = Button(text = 'Add to file', command = save_list)  # Lack single quotes.
    button2.place(x = 250, y = 50, width = 100, height = 25)

    window.mainloop()  # "loop" is wrong.