## Please write a program which asks the user for two numbers and an operation.
# If the operation is add, multiply or subtract, the program should calculate and
# print out the result of the operation with the given numbers.
# If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

## Sample output
# Number 1: -> input: '10'
# Number 2: -> input: '17'
# Operation: -> input: 'add'

# 10 + 17 = 27

## Sample output
# Number 1: -> input: '4'
# Number 2: -> input: '6'
# Operation: -> input: 'multiply'

# 4 * 6 = 24

## Sample output
# Number 1: -> input: '4'
# Number 2: -> input: '6'
# Operation: -> input: 'subtract'

# 4 - 6 = -2


## Solution:
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operation = input("Operation:")

if operation == "add":
    print(f"{number1} + {number2} = {number1+number2}")
if operation == "multiply":
    print(f"{number1} * {number2} = {number1*number2}")
if operation == "subtract":
    print(f"{number1} - {number2} = {number1-number2}")
## Solution:
