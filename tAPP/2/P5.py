'''
Description: Problem 5 (complete the function)
Version: 1.0.1.20210116
Author: Arvin Zhao
Date: 2021-01-15 10:20:02
Last Editors: Arvin Zhao
LastEditTime: 2021-01-16 04:11:03
'''

import random

def pick_number():
    low = int(input('Enter the bottom of the range: '))
    high = int(input('Enter the top of the range: '))
    comp_num = random.randint(low, high)
    return comp_num


def first_guess():
    print('I am thinking of a number...')
    guess = int(input('What am I thinking of: '))
    return guess


def check_answer(comp_num, guess):
    if comp_num == guess:
        print('Correct, you win.')
    else:
        print('Your guess is too low.' if comp_num > guess else 'Your guess is too high.')
        try_again = int(input('Please try again. What am I thinking of: '))
        check_answer(comp_num, try_again)


def main():
    comp_num = pick_number()
    guess = first_guess()
    check_answer(comp_num, guess)


if __name__ == '__main__':  # It is strongly recommended to add this line.
    main()