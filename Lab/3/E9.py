'''
Description: Exercise 9 (Tkinter GUI)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 21:40:01
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 21:04:36
'''

from tkinter import Tk, Label, Entry, Button, Listbox
from tkinter.constants import END


class home:
	'''
	The home window.
	'''

	def __init__(self, root):
		'''
		The constructor of the class.
		'''

		self.root = root
		self.root.title('Number List')
		self.root.geometry('400x200')

		self.label_num= Label(text = 'Enter a number:')
		self.label_num.place(x = 20, y = 20, width = 100, height = 25)

		self.entry_num = Entry()
		self.entry_num.place(x = 120, y = 20, width = 100, height = 25)
		self.entry_num.focus()

		self.button_add = Button(text = 'Add', command = self.add)
		self.button_add.place(x = 250, y = 20, width = 100, height = 25)

		self.listbox_num = Listbox()
		self.listbox_num.place(x = 120, y = 50, width = 100, height = 50)

		self.button_clear = Button(text = 'Clear', command = self.clear)
		self.button_clear.place(x = 250, y = 50, width = 100, height = 50)

		self.button_save = Button(text = 'Save', command = self.save)
		self.button_save.place(x = 250, y = 100, width = 100, height = 50)


	def add(self) -> None:
		'''
		Add a number to the list.
		'''

		num = self.entry_num.get()

		if num.isdigit():
			self.listbox_num.insert(END, num)

		self.entry_num.delete(0, END)


	def clear(self) -> None:
		'''
		Clear the list.
		'''

		self.listbox_num.delete(0, END)
		self.entry_num.focus()


	def save(self) -> None:
		'''
		Save the list to a CSV file.
		'''

		tmp_list = self.listbox_num.get(0, END)
		file = open('num_list.csv', 'w')

		for tmp in tmp_list:
			file.write(tmp + '\n')

		file.close()


window = Tk()
home(window)
window.mainloop()