'''
Description: exercise: Pig Latin
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 07:01:29
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 12:39:43
'''

def do_pig_latin(word: str) -> None:
    '''
    Do Pig Latin on a word.

    Parameters
    ----------
    word : a word for Pig Latin
    '''

    # "aeiou" contains all vowels.
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')


if __name__ == '__main__':
    while True:
        word = input('Enter a word: ').strip().lower()

        if len(word) == 0:
            print('Please do enter something!')
        else:
            do_pig_latin(word)
            break