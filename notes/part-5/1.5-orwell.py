## Please write a program which asks the user for an integer number.
# The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

## Sample output
# Please type in a number: -> input: '2020'

## Sample output
# Please type in a number: -> input: '1984'
# Orwell


## Solution:
number = int(input("Please type in a number:"))
if number == 1984:
        print("Orwell")
