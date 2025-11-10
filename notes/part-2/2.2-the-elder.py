## Please write a program which asks for the names and ages of two persons.
## The program should then print out the name of the elder.

# Some examples of expected behaviour:

## Sample output
# Person 1:
# Name: -> input: 'Alan'
# Age: -> input: '26'
# Person 2:
# Name: -> input: 'Ada'
# Age: -> input: '27'
# The elder is Ada

## Sample output
# Person 1:
# Name: -> input: 'Bill'
# Age: -> input: '1'
# Person 2:
# Name: -> input: 'Jean'
# Age: -> input: '1'
# Bill and Jean are the same age


## Solution:
print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))
print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))
if age1>age2:
    print(f"The elder is {name1}")
elif age2>age1:
    print(f"The elder is {name2}")
elif age1==age2:
    print(f"{name1} and {name2} are the same age")
