'''
Description: exercise: even or odd
Version: 1.0.1.20210114
Author: Arvin Zhao
Date: 2021-01-13 09:55:49
Last Editors: Arvin Zhao
LastEditTime: 2021-01-14 03:52:01
'''

def tell_even_odd(num: int) -> None:
    '''
    Tell whether an integer is even or odd.

    Parameters
    ----------
    num : an integer for judgement.
    '''

    if num % 2 == 0:
        print(num, 'is even.')
    else:
        print(num, 'is odd.')


if __name__ == '__main__':
    while True:
        try:
            tell_even_odd(int(input('Enter an integer: ')))
            break
        except ValueError:
            print('Error! Invalid input!')