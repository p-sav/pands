# convert.py
# program that converts dollars to cent
# author: p-sav

def convert_to_cents(amount):
    # Remove the minus sign if present
    amount = abs(amount)
    # Convert dollars to cents
    cents = int(amount * 100)
    return cents

if __name__ == "__main__":
    # Take input from the user
    amount_dollars = float(input("Enter the amount in dollars: "))
    # Convert dollars to cents
    amount_cents = convert_to_cents(amount_dollars)
    print("The amount in cents:", amount_cents)
