## Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria.
# Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:

## Sample output
# How many times a week do you eat at the student cafeteria? -> input: '4'
# The price of a typical student lunch? -> input: '2.5'
# How much money do you spend on groceries in a week? -> input: '28.5'

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros


## Solution:
cafeteria = int(input("How many times a week do you eat at the student cafeteria?"))
lunch = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure:")
print(f"Daily: {(lunch*cafeteria+groceries)/7} euros")
print(f"Weekly: {(lunch*cafeteria+groceries)} euros")
