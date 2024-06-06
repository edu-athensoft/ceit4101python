"""
string method - capitalize()

string.capitalize()
return a new string

"""

# case 1. capitalize a sentence
str1 = "pyThOn is AWesome."

result = str1.capitalize()

print(f"old string: {str1}")
print(f"new string: {result}")
print()


# case 2. capitalize two sentence
str1 = "pyThOn is AWesome. pyThOn is AWesome."

result = str1.capitalize()

print(f"old string: {str1}")
print(f"new string: {result}")
print()


# case 3. non-alphabetic first character
str1 = "+ pyThOn is AWesome."

result = str1.capitalize()

print(f"old string: {str1}")
print(f"new string: {result}")
print()


# case 4. whitespace as the first character
str1 = " pyThOn is AWesome."

result = str1.capitalize()

print(f"old string: {str1}")
print(f"new string: {result}")
print()


