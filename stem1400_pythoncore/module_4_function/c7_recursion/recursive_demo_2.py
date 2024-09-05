"""
get sum of a sequence
"""


def get_sum(mylist):
    if len(mylist) == 1:
        return mylist[0]

    # mysum = mylist[0] + get_sum(mylist[1:])
    # return mysum
    return mylist[0] + get_sum(mylist[1:])

# main
list1 = [1,2,3,4,5,6,7,8,9,10]
print(get_sum(list1))