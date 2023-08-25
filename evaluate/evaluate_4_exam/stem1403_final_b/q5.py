"""
question 5. Parameter passing

[1, 2, 3],[9, 2, 3],[9, 2, 3],[99, 2, 3]
"""

def foo(mlist):
    mlist[0] = 9
    print(mlist)

mylist = [1,2,3]
print(mylist)
foo(mylist)
print(mylist)
mylist[0] = 99
print(mylist)


