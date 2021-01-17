'''
Description: Problem 4 (complete the code)
Version: 1.0.1.20210117
Author: Arvin Zhao
Date: 2021-01-16 00:19:34
Last Editors: Arvin Zhao
LastEditTime: 2021-01-17 12:01:10
'''

from tkinter import Tk, Label, Entry, Button
from tkinter.constants import END


def convert_to_km():
    miles = textbox1.get()
    message = float(miles) / 1.6093
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, ' km')


def convert_to_miles():
    km = textbox1.get()
    km = int(km)
    message = km * 0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, ' miles')


if __name__ == '__main__':
    window = Tk()
    window.title('Distance')
    window.geometry('260x200')

    label1 = Label(text = 'Enter the value you want to convert: ')
    label1.place(x = 30, y = 20)

    textbox1 = Entry(text = '')
    textbox1.place(x = 30, y = 50, width = 200, height = 25)
    textbox1['justify'] = 'center'
    textbox1.focus()

    convert1 = Button(text = 'Convert mile to km', command = convert_to_km)
    convert1.place(x = 30, y = 80, width = 200, height = 25)
    
    convert2 = Button(text = 'Convert km to mile', command = convert_to_miles)
    convert2.place(x = 30, y = 110, width = 200, height = 25)

    textbox2 = Entry(text = '')
    textbox2.place(x = 30, y = 140, width = 200, height = 25)
    textbox2['justify'] = 'center'

    window.mainloop()