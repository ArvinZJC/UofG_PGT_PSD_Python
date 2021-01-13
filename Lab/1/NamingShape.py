'''
Description: exercise: naming the shape
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 11:04:45
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 11:26:54
'''

def name_shape(slide_num: str, out_of_range_error_msg: str) -> str:
    '''
    Name a shape according to the number of sldies.

    Parameters
    ----------
    slide_num : the number of slides

    out_of_range_error_msg : a specified error message returned if the number of slides is less than 3 or more than 10

    Returns
    -------
    shape : the name of a shape, or an error message
    '''

    shape_namer = {
        '3': 'Triangle',
        '4': 'Square',
        '5': 'Pentagon',
        '6': 'Hexagon',
        '7': 'Heptagon',
        '8': 'Octagon',
        '9': 'Enneagon',
        '10': 'Decagon'
    }
    return shape_namer.get(slide_num, out_of_range_error_msg)  # Return a specified error message if the number of slides is less than 3 or more than 10.


if __name__ == '__main__':
    out_of_range_error_msg = 'Error! Please enter an integer no less than 3 and no more than 10.'

    while True:
        shape = name_shape(input('Enter the number of slides to name a shape: ').strip(), out_of_range_error_msg)
        print(shape)

        if shape != out_of_range_error_msg:
            break