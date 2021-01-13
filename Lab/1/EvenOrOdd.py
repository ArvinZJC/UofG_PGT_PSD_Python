'''
Description: exercise: even or odd
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 09:55:49
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 11:12:07
'''

def tell_even_odd(num: int) -> None:
    '''
    Tell whether an integer is even or odd.

    Parameters
    ----------
    num : an integer for judgement.
    '''

    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    while True:
        try:
            tell_even_odd(int(input('Enter an integer: ')))
            break
        except ValueError:
            print('Error! Invalid input!')