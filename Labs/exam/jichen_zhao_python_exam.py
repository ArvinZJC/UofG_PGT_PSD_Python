'''
Description: the solution to the Python lab exam
Version: 1.0.1.20210304
Author: Jichen Zhao
Date: 2021-02-25 18:29:44
Last Editors: Jichen Zhao
LastEditTime: 2021-03-04 19:35:53
'''

from tkinter import Button, Entry, Frame, Label, messagebox, Scrollbar, Tk, ttk
from tkinter.constants import BOTH, BOTTOM, E, END, HORIZONTAL, N, RIGHT, S, VERTICAL, W, X, Y
import re
import sqlite3


class RegistrationView:
    '''
    The definition of a registration view.
    '''

    def __init__(self, parent: Tk) -> None:
        '''
        The constructor of a registration view to initialise widgets.

        Parameters
        ----------
        parent : the parent window for a registration view to display
        '''

        self.__parent = parent
        screen_width = self.__parent.winfo_screenwidth()
        screen_height = self.__parent.winfo_screenheight()
        parent_width = 600
        parent_height = 400
        self.__db_name = 'Users.db'

        # Intialise the parent window.
        self.__parent.geometry('%dx%d+%d+%d' % (parent_width, parent_height, (screen_width - parent_width) / 2, (screen_height - parent_height) / 2))  # Centre the parent window.
        self.__parent.title('Registration Page')
        self.__parent.minsize(parent_width, parent_height)
        self.__parent.maxsize(int(parent_width * 1.5), int(parent_height * 1.5))

        self.__initialise_widgets()
        self.__initialise_db()

    def __initialise_widgets(self) -> None:
        '''
        Initialise the status of widgets.
        '''

        column_num = 3  # The number of columns for the grid layout.
        padding_x = 15
        padding_y = 20

        # The view uses the grid layout to enable autoresizing.
        for index in range(column_num):
            self.__parent.columnconfigure(index, weight = 0 if index == 0 else 1)

        # New row: the username label and entry.
        row_index = 0  # Make it convenient to index the row of the grid.
        self.__parent.rowconfigure(row_index, weight = 0)

        # Same row, new column: the username label.
        column_index = 0  # Make it convenient to index the column of the grid.
        Label(self.__parent, text = 'Enter your username:').grid(column = column_index, padx = padding_x, pady = padding_y, row = row_index, sticky = W)

        # Same row, new column: the username entry.
        column_index += 1
        self.__entry_username = Entry(self.__parent)
        self.__entry_username.grid(column = column_index, columnspan = column_num - column_index, padx = padding_x, pady = padding_y, row = row_index, sticky = (E, W))

        # New row: the password label and entry.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 0)

        # Same row, new column: the password label.
        column_index = 0
        Label(self.__parent, text = 'Enter your password:').grid(column = column_index, padx = padding_x, row = row_index, sticky = W)

        # Same row, new column: the password entry.
        column_index += 1
        self.__entry_password = Entry(self.__parent)
        self.__entry_password.grid(column = column_index, columnspan = column_num - column_index, padx = padding_x, row = row_index, sticky = (E, W))

        # New row: the save button and the clear button.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 0)
        column_index = 0  # Same row, new column: empty.

        # Same row, new column: the save button.
        column_index += 1
        self.__button_save = Button(self.__parent, command = self.__save, text = 'Save')
        self.__button_save.grid(column = column_index, padx = padding_x, pady = padding_y, row = row_index, sticky = (E, W))

        # Same row, new column: the clear button.
        column_index += 1
        self.__button_clear = Button(self.__parent, command = self.__clear, text = 'Clear')
        self.__button_clear.grid(column = column_index, padx = padding_x, pady = padding_y, row = row_index, sticky = (E, W))

        # New row: placeholder.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 0)
        Label(self.__parent).grid(columnspan = column_num, pady = padding_y / 2, row = row_index)

        # New row: the data table label area.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 0)
        column_index = 0  # Same row, new column: empty.

        # Same row, new column: the data table label.
        column_index += 1
        Label(self.__parent, text = 'Display all usernames and associated passwords in the database').grid(column = column_index, columnspan = column_num - column_index, padx = padding_x, row = row_index, sticky = W)

        # New row: the display button and the data table frame.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 1)

        # Same row, new column: the display button
        column_index = 0
        self.__button_display = Button(self.__parent, command = self.__display, text = 'Display')
        self.__button_display.grid(column = column_index, padx = padding_x, row = row_index, sticky = (E, N, W))

        # Same row, new column: the data table frame
        column_index += 1
        frame_data = Frame(self.__parent)
        frame_data.grid(column = column_index, columnspan = column_num - column_index, padx = padding_x, row = row_index, sticky = (E, N, S, W))

        # In the data table frame: the data table with scrollbars for a better view.
        self.__table_column_list = ['ID', 'Username', 'Password']
        scrollbar_x = Scrollbar(frame_data, orient = HORIZONTAL)
        scrollbar_y = Scrollbar(frame_data, orient = VERTICAL)
        self.__treeview_data = ttk.Treeview(frame_data, columns = self.__table_column_list, show = 'headings', xscrollcommand = scrollbar_x.set, yscrollcommand = scrollbar_y.set)
        scrollbar_x['command'] = self.__treeview_data.xview
        scrollbar_y['command'] = self.__treeview_data.yview
        scrollbar_x.pack(fill = X, side = BOTTOM)
        scrollbar_y.pack(fill = Y, side = RIGHT)
        self.__treeview_data.pack(expand = True, fill = BOTH)

        # New row: placeholder.
        row_index += 1
        self.__parent.rowconfigure(row_index, weight = 0)
        Label(self.__parent).grid(columnspan = column_num, row = row_index)

    def __save(self) -> None:
        '''
        Attempt to save the username and the password to the database.
        '''

        username = self.__entry_username.get()
        password = self.__entry_password.get()

        # Check if the username entered can be unique in the database.
        database = sqlite3.connect(self.__db_name)
        cursor = database.cursor()
        cursor.execute('SELECT * FROM Users WHERE username=:username', {'username': username})

        if len(cursor.fetchall()) != 0:
            messagebox.showwarning('Username error', 'Oops! The username \"' + username + '\" already exists.')
            database.close()
            return

        # Check if the password satisfies the criteria of at least 8 characters which contain at least 1 digit.
        if len(password) >= 8 and bool(re.search(r'\d', password)):
            cursor.execute("INSERT INTO Users(username, password) VALUES('{}', '{}')".format(username, password))
            database.commit()
            database.close()
            return

        database.close()
        messagebox.showwarning('Password error', 'Oops! Your password does not meet the criteria.\nPlease enter a password with at least 8 characters which contain at least 1 digit.')

    def __clear(self) -> None:
        '''
        Clear input and table.
        '''

        self.__entry_username.delete(0, END)
        self.__entry_password.delete(0, END)
        [self.__treeview_data.delete(user) for user in self.__treeview_data.get_children()]
        self.__entry_username.focus()

        for col in self.__table_column_list:
            self.__treeview_data.heading(col, text = '')

    def __display(self) -> None:
        '''
        Display data in the data table.
        '''

        # Retrieve all user data.
        database = sqlite3.connect(self.__db_name)
        cursor = database.cursor()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()
        database.close()

        # Insert data to the data table.
        for col in self.__table_column_list:
            self.__treeview_data.heading(col, text = col)
            self.__treeview_data.column(col, anchor = E, width = 50 if col == self.__table_column_list[0] else 150)

        for user in users:
            self.__treeview_data.insert('', END, values = (user[0], user[1], user[2]))

    def __initialise_db(self) -> None:
        '''
        Create the database or the table if it does not exist.
        '''

        database = sqlite3.connect(self.__db_name)
        cursor = database.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            )''')  # Create the table if it does not exist. The username field should be unique.
        database.commit()
        database.close()


if __name__ == '__main__':
    registration_window = Tk()
    RegistrationView(registration_window)
    registration_window.mainloop()