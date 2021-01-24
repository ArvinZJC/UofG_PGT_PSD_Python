'''
Description: exercise: classifying triangles
Version: 1.0.3.20210124
Author: Arvin Zhao
Date: 2021-01-13 11:27:43
Last Editors: Arvin Zhao
LastEditTime: 2021-01-24 17:36:12
'''

class Triangle:
    '''
    This is a class that can classify a triangle.
    '''

    def __init__(self, side1, side2, side3) -> None:
        '''
        Initialise an instance of the class Triangle.

        Parameters
        ----------
        side1 : the first side of a triangle

        side2 : the second side of a triangle

        side3 : the third side of a triangle
        '''

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    def decide_triangle_type(self) -> str:
        '''
        Decide the type of a triangle according to the length of the 3 sides.
        '''

        # For a triangle, the sum of any 2 sides of a triangle must be greater than the measure of the third side.
        if self.side1 + self.side2 > self.side3 and \
            self.side1 + self.side3 > self.side2 and \
            self.side2 + self.side3 > self.side1:
            if self.side1 == self.side2 == self.side3:
                print('Equilateral triangle')
            elif self.side1 != self.side2 and \
                self.side1 != self.side3 and \
                self.side2 != self.side3:
                print('Scalene triangle')
            else:
                print('Isosceles triangle')
        else:
            print('It cannot be a triangle.')


if __name__ == '__main__':
    while True:
        try:
            side1, side2, side3 = [float(side) for side in input("Enter the length of the 3 sides of a triangle each separated by space: ").split()]

            if side1 > 0 and side2 > 0 and side3 > 0:
                Triangle(side1, side2, side3).decide_triangle_type()
                break
            else:
                raise ValueError
        except ValueError:
            print("Error! Invalid input!")