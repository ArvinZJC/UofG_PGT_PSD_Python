'''
Description: Problem 4. Debugging code (correct errors)
Version: 1.0.0.20210115
Author: Arvin Zhao
Date: 2021-01-15 09:50:36
Last Editors: Arvin Zhao
LastEditTime: 2021-01-15 13:20:09
'''

import random

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)  # "randit" is wrong.
    print(num1, '+', num2, '=')
    user_answer = int(input('Your answer: '))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers  # "answer" is wrong.


def subtraction():
    num3 = random.randint(25, 50)
    num4 = random.randint(1, 25)  # "random.random" is not suitable here.
    print(num3, '-', num4)
    user_answer = int(input('Your answer: '))
    actual_answer = num3 - num4  # "==" is wrong.
    answers = (user_answer, actual_answer)  # Redundant colon.
    return answers


def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print('Correct')
    else:  # Improper indent.
        print('Incorrect, the answer is', actual_answer)


def main():
    print('1) Addition')
    print('2) Subtraction')
    selection = int(input('Enter 1 or 2: '))
    if selection == 1:  # "=" is wrong.
        user_answer, actual_answer = addition()  # "user_answers" is wrong.
        check_answer(user_answer, actual_answer)
    elif selection == 2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)  # Lack a necessary comma.
    else:  # Improper indent.
        print('Incorrect selection.')

    
if __name__ == '__main__':  # It is strongly recommended to add this line.
    main()