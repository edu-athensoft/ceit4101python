"""
string method - count()

string.count(substring [, start=... [, end=...]])
return how many times the substring si present in the original string
"""

# case 1. only with substring
str1 = "Python is awesome, isn't it? Python is awesome, isn't it? Python is awesome, isn't it?"
substring = 'is'

count = str1.count(substring)

print(f"The count is: {count}")
print()


# case 2. with substring ,start
str1 = "Python is awesome, isn't it? Python is awesome, isn't it? Python is awesome, isn't it?"
substring = 'is'

count = str1.count(substring, 16 )

print(f"The count is: {count}")
print()


# case 3. with substring ,start, end
str1 = "Python is awesome, isn't it? Python is awesome, isn't it? Python is awesome, isn't it?"
substring = 'is'

count = str1.count(substring, 16, 32 )

print(f"The count is: {count}")
print()