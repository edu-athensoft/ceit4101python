"""
iterable
"""

mylist = [1, 2, 3]

# get iterator of an iterable object
mylist_iterator = iter(mylist)

while True:
    try:
        item = next(mylist_iterator)
        print(item)
    except StopIteration as se:
        # print(se)
        break



