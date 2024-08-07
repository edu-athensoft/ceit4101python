"""
7. Write code to count the number of occurrences of
a specified character of a string without using string APIs.
Sample input:  'Apple',  'p'
Sample output:  2
"""


def count(mystr, mychar):
    num = 0
    for c in mystr:
        if c == mychar:
            num += 1
    return num

# test
print(count('Apple',  'p'))


