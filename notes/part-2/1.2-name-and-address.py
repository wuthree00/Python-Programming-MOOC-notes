## Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

## Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

## Solution:
given_name = input("Given name: ")
#print("Given name: "+given_name) -> debugging check
family_name = input("Family name: ")
#print("Family name: "+family_name) -> debugging check
street_address = input("Street address: ")
#print("Street address: "+street_address) -> debugging check
city_postal_code = input("City and postal code: ")
#print("City and postal code: "+city_postal_code) -> debugging check
print(given_name+" "+family_name)
print(street_address)
print(city_postal_code)
