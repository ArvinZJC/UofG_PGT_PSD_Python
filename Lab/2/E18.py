'''
Description: Exercise 18 (dictionary)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 11:34:21
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 13:36:15
'''

food_dictionary = {
    1: input('Enter the first of your favourite foods: ').strip(),
    2: input('Enter the second of your favourite foods: ').strip(),
    3: input('Enter the third of your favourite foods: ').strip(),
    4: input('Enter the fourth of your favourite foods: ').strip()
}
print(food_dictionary)

del food_dictionary[int(input('Which one do you want to get rid of? Enter the number: '))]  # "dictionary.pop(key)" can also be used to remove a key-value pair from a dictiionary.
print(sorted(food_dictionary.values()))