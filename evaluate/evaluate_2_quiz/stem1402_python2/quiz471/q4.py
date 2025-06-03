"""
Write a program to find the max number in a given list using recursion.

The signature of the function is:
find_max(your_list)
return:  int

Example:
find_max([3, 7, 1, 9, 4, 6])
return:  9
"""

def find_max(mylist):
    if len(mylist) == 1:
        return mylist[0]

    return max(mylist[0], find_max(mylist[1:]))


result = find_max([3, 70, 1, 9, 4, 6])
print(result)
