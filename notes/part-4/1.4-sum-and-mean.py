## Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

# The program should function as follows:

## Sample output
# Number 1: -> input: '2'
# Number 2: -> input: '1'
# Number 3: -> input: '6'
# Number 4: -> input: '7'
# The sum of the numbers is 16 and the mean is 4.0


## Solution:
n1=int(input("Number 1:"))
n2=int(input("Number 2:"))
n3=int(input("Number 3:"))
n4=int(input("Number 4:"))
print(f"The sum of the numbers is {n1+n2+n3+n4} and the mean is {(n1+n2+n3+n4)/4}")
