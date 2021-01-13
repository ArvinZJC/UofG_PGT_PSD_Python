'''
Description: exercise: day old bread
Version: 1.0.0.20210113
Author: Arvin Zhao
Date: 2021-01-13 06:12:15
Last Editors: Arvin Zhao
LastEditTime: 2021-01-13 10:28:04
'''

def print_receipt(loaf_num: int, regular_per_price: float, discount_percentage: float) -> None:
    '''
    Calculate and print the regular price for loaves of bread, as well as the discount and the actual price for the day old bread.

    Parameters
    ----------
    loaf_num : the number of loaves of day old bread

    regular_per_price : the regular price for loaves of bread for each

    discount_percentage : the percentage of the discount for the day old bread
    '''

    regular_price = loaf_num * regular_per_price  # Calculate the regular price for loaves of bread.
    discount = regular_price * (1 - discount_percentage)  # Calculate the discount for the bread because of a day old.
    total_price = regular_price - discount  # Calculate the actual price for the day old bread.
    print('Regular price:', '%.2f' % regular_price)
    print('Discount:', '- %.2f' % discount)
    print('Total price:', '%.2f' % total_price)


if __name__ == '__main__':
    while True:
        loaf_num = input('Enter the number of loaves of day old bread being purchased: ')

        if loaf_num.isdigit():
            print_receipt(int(loaf_num), 3.49, 0.6)
            break
        else:
            print('Error! Non-negative integer please!')