# lab3.1.div.py
# program that divides one number into the other and displays the remainder
# author: p-sav

x = int(input("Enter the first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the integer division
remainder = x%y # % gives the remainder

print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))
