'''
Description: Exercise 14 (Tkinter GUI)
Version: 1.0.1.20210124
Author: Arvin Zhao
Date: 2021-01-19 16:59:37
Last Editors: Arvin Zhao
LastEditTime: 2021-01-24 17:33:43
'''

from tkinter import Tk, OptionMenu, StringVar


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

		OPTIONS = ['red', 'orange', 'blue', 'green']

		self.root = root
		self.root.title('Colours')
		self.root.geometry('400x200')
		self.root['bg'] = OPTIONS[0]

		self.variable_colours = StringVar(root)
		self.variable_colours.set(OPTIONS[0])
		self.option_menu_colours = OptionMenu(root, self.variable_colours, *OPTIONS)
		self.option_menu_colours.place(x = 120, y = 80, width = 100, height = 25)
		self.variable_colours.trace_variable('w', self.change_bg)


	def change_bg(self) -> None:
		'''
		Change the background colour of the window according to the user's choice.
		'''

		self.root['bg'] = self.variable_colours.get()


window = Tk()
Home(window)
window.mainloop()	