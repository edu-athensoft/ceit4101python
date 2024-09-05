"""
get factorial of a sequence
"""


def factorial(mylist):
    if len(mylist) == 1:
        return mylist[0]

    return mylist[0] * factorial(mylist[1:])

# main
list1 = [1,2,3,4,5,6,7,8,9,10]
print(factorial(list1))