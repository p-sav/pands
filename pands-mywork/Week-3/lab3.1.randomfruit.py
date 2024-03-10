# randomfruit.py
# this program prints out random fruit
# author:p-sav

import random 
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# random number between 0 and length -1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A Random Fruit: {}".format(fruit))

