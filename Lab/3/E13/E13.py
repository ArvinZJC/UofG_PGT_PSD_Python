'''
Description: Exercise 13 (Tkinter GUI)
Version: 1.0.0.20210119
Author: Arvin Zhao
Date: 2021-01-19 15:57:06
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 17:38:23
'''

from tkinter import StringVar, Tk, Label, PhotoImage, Entry, Button
from tkinter.constants import END
import random


class home:
	'''
	The home window.
	'''

	def __init__(self, root):
		'''
		The constructor of the class.
		'''
		
		self.root = root
		self.root.title("Addition")
		self.root.geometry("400x300")

		self.image_tick = PhotoImage(file = 'tick.png')
		self.label_tick = Label(image = self.image_tick)

		self.image_cross = PhotoImage(file = 'cross.png')
		self.label_cross = Label(image = self.image_cross)

		self.num1 = random.randint(10, 50)
		self.num2 = random.randint(10, 50)
		self.text_question = StringVar()
		self.text_question.set(str(self.num1) + ' + ' + str(self.num2) + ' =')
		self.label_question = Label(textvariable = self.text_question)
		self.label_question.place(x = 20, y = 20, width = 100, height = 25)

		self.entry_answer = Entry()
		self.entry_answer.place(x = 140, y = 20, width = 100, height = 25)
		self.entry_answer.focus()

		self.button_submit = Button(text = 'Submit', command = self.check)
		self.button_submit.place(x = 260, y = 20, width = 100, height = 25)

		self.button_next = Button(text = 'Next', command = self.generate_question)
		self.button_next.place(x = 260, y = 100, width = 100, height = 25)


	def check(self) -> None:
		'''
		Check if the answer is correct.
		'''

		try:
			if int(self.entry_answer.get()) == self.num1 + self.num2:
				self.label_tick.place(x = 20, y = 100, width = 100, height = 100)
				self.label_cross.place_forget()
			else:
				self.label_cross.place(x = 20, y = 100, width = 100, height = 100)
				self.label_tick.place_forget()
		except ValueError:
			self.label_cross.place(x = 20, y = 100, width = 100, height = 100)
			self.label_tick.place_forget()


	def generate_question(self) -> None:
		'''
		Generate a new addition question.
		'''

		self.num1 = random.randint(10, 50)
		self.num2 = random.randint(10, 50)
		self.text_question.set(str(self.num1) + ' + ' + str(self.num2) + ' =')
		self.entry_answer.delete(0, END)
		self.label_tick.place_forget()
		self.label_cross.place_forget()


window = Tk()
home(window)
window.mainloop()