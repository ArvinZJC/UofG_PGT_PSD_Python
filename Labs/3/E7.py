'''
Description: Exercise 7 (Tkinter GUI)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 21:04:02
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 21:27:10
'''

from tkinter import Tk, Entry, Label, DoubleVar, Button
from tkinter.constants import END


def add() -> None:
    '''
    Add a number to the total.
    '''

    try:
        num = float(entry_num.get())
    except ValueError:
        num = 0

    entry_num.delete(0, END)
    total = total_text.get() + num
    total_text.set(total)


def reset() -> None:
    '''
    Reset the program.
    '''

    entry_num.delete(0, END)
    total_text.set(0)


if __name__ == '__main__':
    window = Tk()
    window.title('Sum')
    window.geometry('300x300')

    entry_num = Entry()
    entry_num.pack()
    entry_num.focus()

    total_text = DoubleVar()
    total_text.set(0)
    label_total = Label(textvariable = total_text)
    label_total.pack()

    button_add = Button(text = 'Add', command = add)
    button_add.pack()

    button_reset = Button(text = 'Reset', command = reset)
    button_reset.pack()

    window.mainloop()