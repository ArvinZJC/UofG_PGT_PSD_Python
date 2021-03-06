'''
Description: Exercise 15 (turtle graphics)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 05:31:59
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 10:59:20
'''

import turtle, random


turtle.shape(random.choice(['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']))

for count in range(random.randint(2, 10)):
    turtle.forward(random.randint(50, 200))
    turtle.right(random.randint(1, 360))

turtle.mainloop()