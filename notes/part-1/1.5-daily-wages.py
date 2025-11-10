## Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

## Sample output
# Hourly wage: -> input: '8.5'
# Hours worked: -> input: '3'
# Day of the week: -> input: 'Monday'
# Daily wages: 25.5 euros'

## Sample output
# Hourly wage: -> input: '12.5'
# Hours worked: -> input: '10'
# Day of the week: -> input: 'Sunday'
# Daily wages: 250.0 euros


## Solution:
hourly_wage=float(input("Hourly wage:"))
hours_worked=int(input("Hours worked:"))
day=input("Day of the week:")
if day == "Sunday":
    print(f"Daily wages: {float(hourly_wage*hours_worked*2)} euros")
elif day != "Sunday":
    print(f"Daily wages: {float(hourly_wage*hours_worked)} euros")
