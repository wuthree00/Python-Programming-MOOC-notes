## Please write a program which asks for two integer numbers.
## The program should then print out whichever is greater.
## If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

## Sample output
# Please type in the first number: -> input: '5'
# Please type in another number: -> input: '3'
# The greater number was: 5

## Sample output
# Please type in the first number: -> input: '5'
# Please type in another number: -> input: '8'
# The greater number was: 8

## Sample output
# Please type in the first number: -> input: '5'
# Please type in another number: -> input: '5'
# The numbers are equal!


## Solution:
number1 = int(input("Please type in the first number:"))
number2 = int(input("Please type in another number:"))
if number1 > number2:
    print(f"The greater number was {number1}")
elif number2 > number1:
    print(f"The greater number was {number2}")
elif number2 == number1:
    print("The numbers are equal!")
