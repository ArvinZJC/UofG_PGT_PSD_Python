'''
Description: Exercise 14 (turtle graphics)
Version: 1.0.0.20210118
Author: Arvin Zhao
Date: 2021-01-18 05:15:35
Last Editors: Arvin Zhao
LastEditTime: 2021-01-18 10:57:45
'''

import turtle, random


turtle.shape(random.choice(['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']))

# Draw an octagon.
for count in range(8):
    turtle.color(random.choice(['green', 'blue', 'red', 'orange', 'brown', 'purple']))
    turtle.forward(100)
    turtle.right(45)

turtle.mainloop()