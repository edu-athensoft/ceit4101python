"""
string method - casefold()

string.casefold()
is an aggressive lower() method which converts strings to case folded strings for caseless matching

"""

# case 1. lowercase
str1 = 'PYTHON IS AWESOME.'
result = str1.casefold()
print(f"The old str is: {str1}")
print(f"The result is: {result}")
print()


# case 2. aggressive lowercase
str2 = 'der Fluß'
# str2 = 'É'
result = str2.casefold()
print(f"The old str is: {str2}")
print(f"The result is: {result}")
print()


# case 3.
first_str = 'der Fluß'
second_str = 'der Fluss'

if first_str.casefold() == second_str.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')

if first_str == second_str:
    print('The strings are equal.')
else:
    print('The strings are not equal.')

