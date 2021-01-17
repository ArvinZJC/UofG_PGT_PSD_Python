'''
Description: Exercise 1. Slicing
Version: 1.0.3.20210117
Author: Arvin Zhao
Date: 2021-01-12 04:01:07
Last Editors: Arvin Zhao
LastEditTime: 2021-01-17 12:12:28
'''

def get_line() -> str:
    '''
    Get input for the first line of a favourite song.

    Returns
    -------
    line : input for the first line of a favourite song
    '''

    while True:
        line = input('Enter the first line of your favourite song: ')
        line_len = len(line)
        print('Input length:', line_len)

        if line_len == 0:
            print('Please do enter something!')
        else:
            break

    return line


def get_start() -> int:
    '''
    Get a starting number.

    Returns
    -------
    start : a starting number
    '''

    while True:
        start = input('Enter a starting number: ')

        if len(start.strip()) == 0:
            start = None
            break
        else:
            try:
                start = int(start)
                break
            except ValueError:
                print('Error! Integer please!')

    return start


def get_end() -> int:
    '''
    Get an ending number.

    Returns
    -------
    end : an ending number
    '''

    while True:
        end = input('Enter an ending number: ')

        if len(end.strip()) == 0:
            end = None
            break
        else:
            try:
                end = int(end)
                break
            except ValueError:
                print('Error! Integer please!')


if __name__ == '__main__':
    line = get_line()
    print('Your preferred section:', line[get_start():get_end()])