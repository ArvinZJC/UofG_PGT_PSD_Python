'''
Description: Exercise 6 (Tkinter GUI)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 20:38:59
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 21:08:31
'''

from tkinter import Tk, Label, StringVar, Button
import random


def roll_dice() -> None:
    '''
    Roll the dice.
    '''

    point.set(random.randint(1, 6))


if __name__ == '__main__':
    window = Tk()
    window.title('Dice')
    window.geometry('200x200')

    point = StringVar()
    point.set('?')
    label_point = Label(textvariable = point)
    label_point.pack()

    button_roll = Button(text = 'Click me to roll the dice', command = roll_dice)
    button_roll.pack()

    window.mainloop()