'''
Description: Exercise 7 (function)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 03:20:05
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 03:34:09
'''

def get_num() -> int:
    '''
    Get a number from the user.

    Returns
    -------
    num : a number from the user
    '''

    return int(input('Enter a number: '))


def count(num: int) -> None:
    '''
    Count 1 to a specified number.

    Parameters
    ----------
    num : a specified number
    '''

    if num > 1:
        for count in range(num):
            print(count + 1)
    else:
        for count in range(len(range(num, 2))):
            print(1 - count)


if __name__ == '__main__':
    count(get_num())