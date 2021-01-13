'''
Description: exercise: your age
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 09:44:34
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 10:27:55
'''

def check_age(age: int) -> None:
    '''
    Check an age and print what he/she can do regarding the age.

    Parameters
    ----------
    age : his/her age for checking what he/she can do
    '''

    if age >= 18:
        print('You can vote.')
    elif age == 17:
        print('You can learn how to drive.')
    elif age == 16:
        print('You can buy a lottery ticket.')
    else:
        print('You can go Trick-or-Treating.')


if __name__ == '__main__':
    while True:
        age = input('Enter your age: ')

        if age.isdigit():
            check_age(int(age))
            break
        else:
            print('Error! Invalid input!')