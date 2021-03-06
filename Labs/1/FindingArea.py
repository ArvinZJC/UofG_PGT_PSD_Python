'''
Description: exercise: finding the area
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 12:20:06
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 12:48:56
'''

def display_square_area() -> None:
    '''
    Calculate and display the area of a square.
    '''

    while True:
        try:
            side = float(input('Enter the length of a square\'s side: '))
            print('Area:', side * side)  # Calculate the area of a square by the formula "side length * side length".
            break
        except ValueError:
            print('Error! Invalid input!')


def display_triangle_area() -> None:
    '''
    Calculate and display the area of a triangle.
    '''

    while True:
        try:
            base, height = [float(value) for value in input("Enter the base and height separated by space: ").split()]

            if base > 0 and height > 0:
                print('Area:', base * height / 2)  # Calculate the area of a triangle by the formula "base * height / 2".
                break
            else:
                raise ValueError
        except ValueError:
            print('Error! Invalid input!')


if __name__ == '__main__':
    print('1) Square')
    print('2) Triangle')

    while True:
        choice = input('Enter 1 or 2 as your choice: ').strip()

        if choice == '1':
            display_square_area()
            break
        elif choice == '2':
            display_triangle_area()
            break
        else:
            print('Error! No such option!')