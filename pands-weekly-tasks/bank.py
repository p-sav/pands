# bank.py
# Program that prompts a user and adds two money amounts 
# author: p-sav


num1 = int(input("Enter amount 1 (in cent) "))
num2 = int(input ("Enter amount 2 (in cent) "))
result = (num1 + num2)

result_in_euros = result / 100

print ("sum: €", result_in_euros)


