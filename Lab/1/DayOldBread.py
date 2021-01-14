'''
Description: exercise: day old bread
Version: 1.0.1.20210114
Author: Arvin Zhao
Date: 2021-01-13 06:12:15
Last Editors: Arvin Zhao
LastEditTime: 2021-01-14 03:49:47
'''

def print_receipt(loaf_num: int, regular_per_price: float, discount_rate: float) -> None:
    '''
    Calculate and print the regular price for loaves of bread, as well as the discount and the actual price for the day old bread.

    Parameters
    ----------
    loaf_num : the number of loaves of day old bread

    regular_per_price : the regular price for loaves of bread for each

    discount_rate : the rate of the discount for the day old bread
    '''

    regular_price = loaf_num * regular_per_price  # Calculate the regular price for loaves of bread.
    discount = regular_price * discount_rate  # Calculate the discount for the bread because of a day old.
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