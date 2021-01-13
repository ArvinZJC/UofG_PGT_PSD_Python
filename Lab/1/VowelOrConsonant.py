'''
Description: exercise: vowel or consonant
Version: 
Author: Arvin Zhao
Date: 2021-01-13 10:24:55
Last Editors: 
LastEditTime: 2021-01-13 11:04:17
'''

def tell_vowel_consonant(letter: str) -> None:
    '''
    Tell whether a letter is a vowel or a consonant.

    Parameters
    ----------
    letter : a letter for judgement
    '''

    if letter in 'aeiou':
        print('The letter is a vowel.')
    elif letter == 'y':
        print('The letter is a vowel, and sometimes a consonant.')
    else:
        print('The letter is a consonant.')


if __name__ == '__main__':
    while True:
        letter = input('Enter a letter of the alphabet: ').strip().lower()

        if len(letter) == 1 and letter.isalpha():
            tell_vowel_consonant(letter)
            break
        else:
            print('Error! Invalid input!')