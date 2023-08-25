"""
Write a Python program to generate all sublists of a list.
No. 33 w3rsc
"""

from itertools import combinations
def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs


# main
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']

print("Original list:")
print(l1)
print("Sublists of the said list:")
print(sub_lists(l1))

print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))