"""
quiz 332

5. Write a program to count the number of times that a specified character appears in a string input by user.
Sample input:
Enter a string: Python is a general-purpose programming language.
Enter a char: p

Sample output:
3

"""

import sys

MYSTR = "Python is a general-purpose programming language."

CHAR = input("Enter a char:")

if len(CHAR) == 0:
    print("No input! Exiting...")
    sys.exit()

# get the first char
CHAR = CHAR[0]


# if we do not know the String API  lower() or upper()
count = 0

# the difference between lower-case letter and upper-case one
DIFF = 32

for char in MYSTR:
    # print(char)
    if ord(CHAR) == ord(char):
        count += 1
    if min(ord(CHAR), ord(char)) + DIFF == max(ord(CHAR), ord(char)):
        count += 1

print(MYSTR)
print(f"Total number of char {CHAR} is: {count}")


# print(ord('P'))
# print(ord('p'))
