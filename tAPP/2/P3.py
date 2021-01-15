'''
Description: Problem 3 (rearrange the code)
Version: 1.0.0.20210114
Author: Arvin Zhao
Date: 2021-01-14 22:51:16
Last Editors: Arvin Zhao
LastEditTime: 2021-01-14 23:55:46
'''

def get_data():
    username = input('Enter your username: ')
    age = int(input('Enter your age: '))
    data_tuple = (username, age)
    return data_tuple


def message(username, age):
    if age <= 10:
        print('Hi', username)
    else:
        print('Hello', username)


def main():
    username, age = get_data()
    message(username, age)


if __name__ == '__main__':
    main()