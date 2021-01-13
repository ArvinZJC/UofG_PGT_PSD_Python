'''
Description: Exercise 2. Umbrella or no umbrella
Version: 1.0.1.20210112
Author: Arvin Zhao
Date: 2021-01-12 04:24:16
Last Editors: Arvin Zhao
LastEditTime: 2021-01-12 06:26:27
'''

if input('Is it raining?  ').lower().strip() == 'yes':
    print('It\'s too windy for an umbrella.' if input('Is it windy?  ').lower().strip() == 'yes' else 'Take an umbrella!')
else:
    print('Enjoy your day!')