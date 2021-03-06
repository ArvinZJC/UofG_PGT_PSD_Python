'''
Description: Exercise 19 (tuple)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 13:36:27
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 13:43:48
'''

country_tuple = ('China', 'USA', 'UK', 'Canada', 'Australia')
print(country_tuple)

country = input('Select a country from the tuple: ').strip()
print(country, 'has the index number', country_tuple.index(country))

index = int(input('Enter an index number between 0 and 4: '))
print(country_tuple[index])