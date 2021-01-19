'''
Description: Exercises 10 & 11 (Tkinter GUI)
Version: 1.0.0.20210119
Author: Arvin Zhao
Date: 2021-01-19 09:00:15
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 21:00:01
'''

from tkinter import StringVar, Tk, Label, Entry, Listbox, Button
from tkinter.constants import END
import csv


class home:
	'''
	The home window.
	'''

	def __init__(self, root):
		'''
		The constructor of the class.
		'''

		self.root = root
		self.root.title('Names and Ages')
		self.root.geometry('400x300')

		self.label_name = Label(text = 'Enter a name:')
		self.label_name.place(x = 20, y = 20, width = 100, height = 25)

		self.entry_name = Entry()
		self.entry_name.place(x = 120, y = 20, width = 100, height = 25)
		self.entry_name.focus()

		self.label_age = Label(text = 'Enter an age:')
		self.label_age.place(x = 20, y = 50, width = 100, height = 25)

		self.entry_age = Entry()
		self.entry_age.place(x = 120, y = 50, width = 100, height = 25)
		self.entry_age.focus()

		self.note_text = StringVar()
		self.label_note = Label(textvariable = self.note_text, fg = 'red')
		self.label_note.place(x = 20, y = 80, width = 200, height = 25)

		self.listbox_content = Listbox()
		self.listbox_content.place(x = 120, y = 110, width = 100, height = 100)

		self.button_save = Button(text = 'Save', command = self.save)
		self.button_save.place(x = 250, y = 20, width = 100, height = 50)

		self.button_display = Button(text = 'Show', command = self.display)
		self.button_display.place(x = 250, y = 110, width = 100, height = 50)


	def save(self) -> None:
		'''
		Save the name and the age to the file.
		'''

		name = self.entry_name.get()
		age = self.entry_age.get()
		is_invalid_age = False

		try:
			age = int(age)

			if age < 0:
				raise ValueError
		except ValueError:
			is_invalid_age = True

		if name == '' or is_invalid_age:
			self.note_text.set('Error! Invalid input.')
		else:
			self.note_text.set('')
			self.entry_name.delete(0, END)
			self.entry_age.delete(0, END)

			data = tuple((name, age))

			file = open(file_name, 'a')
			writer = csv.writer(file, lineterminator = '\n')
			writer.writerow(data)
			file.close()


	def display(self) -> None:
		'''
		Display the content of the file in a list box.
		'''

		file = open(file_name, 'r')
		self.listbox_content.delete(0, END)

		for content in csv.reader(file):
			self.listbox_content.insert(END, content)


file_name = 'name_age_list.csv'

window = Tk()
home(window)
window.mainloop()