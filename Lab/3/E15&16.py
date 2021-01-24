'''
Description: Exercises 15 & 16 (Tkinter GUI)
Version: 1.0.2.20210124
Author: Arvin Zhao
Date: 2021-01-19 17:18:58
Last Editors: Arvin Zhao
LastEditTime: 2021-01-24 17:23:09
'''

from tkinter import Button, Tk, Label, Entry, StringVar, OptionMenu, Listbox
from tkinter.constants import END


class Home:
	'''
	The home window.
	'''

	def __init__(self, root) -> None:
		'''
		The constructor of the class.

		Parameters
		----------
		root : the parent window or frame for the home window to display.
		'''

		self.root = root
		self.root.title('Name & Gender')
		self.root.geometry('300x300')

		self.label_name = Label(text = 'Enter a name:')
		self.label_name.place(x = 20, y = 50, width = 100, height = 25)

		self.entry_name = Entry()
		self.entry_name.place(x = 150, y = 50, width = 100, height = 25)
		self.entry_name.focus()

		self.label_gender = Label(text = 'Choose a gender')
		self.label_gender.place(x = 20, y = 100, width = 100, height = 25)

		self.OPTIONS = ['Male', 'Female', 'Other']

		self.variable_gender = StringVar(root)
		self.variable_gender.set(self.OPTIONS[0])
		self.option_menu_gender= OptionMenu(root, self.variable_gender, *self.OPTIONS)
		self.option_menu_gender.place(x = 150, y = 100, width = 100, height = 25)

		self.button_add = Button(text = 'Add', command = self.add)
		self.button_add.place(x = 20, y = 150, width = 100, height = 25)

		self.button_display = Button(text = 'Display', command = self.display)
		self.button_display.place(x = 20, y = 180, width = 100, height = 25)

		self.listbox_content = Listbox()
		self.listbox_content.place(x = 150, y = 150, width = 100, height = 100)

		self.file_name = 'name_gender_list.txt'


	def add(self) -> None:
		'''
		Add a name and a gender to the list box.
		'''

		name = self.entry_name.get()

		if name != '':
			content = name + ', ' + self.variable_gender.get() + '\n'
			self.listbox_content.insert(END, content)
			self.entry_name.delete(0, END)
			self.variable_gender.set(self.OPTIONS[0])

			file = open(self.file_name, 'a')
			file.write(content)
			file.close()


	def display(self) -> None:
		'''
		Display the entire text file in the console.
		'''

		file = open(self.file_name, 'r')
		print(file.read())
		file.close()


window = Tk()
Home(window)
window.mainloop()