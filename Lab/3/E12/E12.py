'''
Description: Exercise 12 (Tkinter GUI)
Version: 1.0.0.20210119
Author: Arvin Zhao
Date: 2021-01-19 14:04:51
Last Editors: Arvin Zhao
LastEditTime: 2021-01-19 21:00:23
'''

from tkinter import Message, PhotoImage, Tk, Label, Entry, Button


def press() -> None:
    '''
    Update the message when clicking on the button.
    '''

    name = entry_name.get()
    message_welcome['text'] = 'Hello, ' + entry_name.get() + '!' if name != '' else '(Sorry, but what is your name?)'


if __name__ == '__main__':
    window = Tk()
    window.title('List of Names')
    window.geometry('450x350')
    window.wm_iconbitmap('Dunno.ico')
    window.configure(bg = 'black')

    image_logo = PhotoImage(file = 'Meme.gif')
    label_logo = Label(image = image_logo)  # You can import a GIF or PNG image if you use Tkinter 8.6 or above. Otherwise, only GIF images are acceptable.
    label_logo.place(x = 100, y = 20, width = 200, height = 150)

    label_name = Label(text = 'Enter your name:', bg = 'black', fg = 'white')
    label_name.place(x = 30, y = 200)

    entry_name = Entry()
    entry_name.place(x = 150, y = 200, width = 180, height = 25)
    entry_name.focus()

    button_press = Button(text = 'Press me', bg = 'yellow', command = press)
    button_press.place(x = 30, y = 250, width = 120, height = 25)

    message_welcome = Message(aspect = 400)
    message_welcome.place(x = 150, y = 250, width = 200, height = 25)

    window.mainloop()