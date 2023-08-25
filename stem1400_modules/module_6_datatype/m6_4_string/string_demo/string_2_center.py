"""
string method - center()

string.center(width [,fillchar])
to make a string centered

"""

# case 1. only with width
str1 = 'cat'
print(f"|{str1}|")

result = str1.center(9)
print(f"result is: {result}")
print(f"result is: |{result}|")
print()

print(f"result is: |{str1:^9}|")
print("result is: |{:^9}|".format(str1))


# case 2.
str1 = 'cat'
result = str1.center(8)
print(f"result is: |{result}|")
print()


# case 3. with fillchar
str1 = 'cat'
result = str1.center(9,'*')
print(f"result is: |{result}|")