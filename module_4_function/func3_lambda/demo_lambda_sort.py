"""
demo of lambda

sorting

"""

mylist = ["a z", "c y", "b x", "d w"]

# sorting by default, ascending
mylist.sort()
print(mylist)
print()

# sorting by last name, ascending
mylist.sort(key=lambda name: name.split(" ")[-1].lower())
print(mylist)
print()

# sorting by default, descending
mylist.sort()
print(mylist)
print()

# sorting by last name, descending
mylist.sort(reverse=True)
print(mylist)
print()