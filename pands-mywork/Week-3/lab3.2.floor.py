# floor.py
# program that takes in a float and outputs an integer rounded down
# author: p-sav

import math
numbertofloor = float(input('Enter a float number:"'))
floorednumber = math.floor(numbertofloor)
print('{} floored is {}'.format(numbertofloor, floorednumber))
