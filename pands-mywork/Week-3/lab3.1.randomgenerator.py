# lab3.1.randomgenerator.py
# program that generates a random number 
# author: p-sav]

'''
import random
number = random.randint(1,10)
print("Here is a random number {}".format(number))
'''

import random

def generate_random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

if __name__ == "__main__":
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    if lower_bound >= upper_bound:
        print("Error: Lower bound must be less than upper bound.")
    else:
        random_number = generate_random_number(lower_bound, upper_bound)
        print("Random number between", lower_bound, "and", upper_bound, ":", random_number)

