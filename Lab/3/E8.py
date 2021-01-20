'''
Description: Exercise 8 (Tkinter GUI)
Version: 1.0.1.20210119
Author: Arvin Zhao
Date: 2021-01-18 21:27:18
Last Editors: Arvin Zhao
LastEditTime: 2021-01-20 13:49:46
'''

from tkinter import Tk, Label, Entry, Button, Listbox
from tkinter.constants import END


class Home:
    '''
    The home window.
    '''

    def __init__(self, root):
        '''
        The constructor of the class.
        '''

        self.root = root
        self.root.title('Name List')
        self.root.geometry('400x200')

        self.label_name = Label(text = 'Enter your name:')
        self.label_name.place(x = 20, y = 20, width = 100, height = 25)

        self.entry_name = Entry()
        self.entry_name.place(x = 120, y = 20, width = 100, height = 25)
        self.entry_name.focus()

        self.button_add = Button(text = 'Add', command = self.add)
        self.button_add.place(x = 250, y = 20, width = 100, height = 25)

        self.listbox_name = Listbox()
        self.listbox_name.place(x = 120, y = 50, width = 100, height = 50)

        self.button_clear = Button(text = 'Clear', command = self.clear)
        self.button_clear.place(x = 250, y = 50, width = 100, height = 50)


    def add(self) -> None:
        '''
        Add a name to the list.
        '''

        name = self.entry_name.get()
        self.listbox_name.insert(END, name)
        self.entry_name.delete(0, END)


    def clear(self) -> None:
        '''
        Clear the list.
        '''

        self.listbox_name.delete(0, END)
        self.entry_name.focus()


window = Tk()
Home(window)
window.mainloop()