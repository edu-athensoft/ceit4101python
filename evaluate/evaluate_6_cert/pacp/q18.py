"""
18. How many elements will the list2 list contain after execution of the following snippet?
list1 = [False for i in range(1, 10)]
list2 = list1[-1: 1: -1]
A. zero
B. five
C. seven
D. three

"""

list1 = [False for i in range(1, 10)]
list1 = [i for i in range(1, 10)]
list2 = list1[-1: 1: -1]

print(f"list1={list1}")
print(f"list2={list2}")

