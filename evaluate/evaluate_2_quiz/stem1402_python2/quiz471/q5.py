"""
5. Write a program to find the min number in a given list iteratively.
The signature of the function is:
find_max(your_list)
return: int

Example:
find_min([3, 7, 1, 9, 4, 6])
return: 1
"""

def find_min(mylist):
    if len(mylist) == 1:
        return mylist[0]

    return min(mylist[0], find_min(mylist[1:]))


result = find_min([3, 70, 1, 9, 4, 6])
print(result)