"""
print a sequence
"""

def show_seq(mylist):
    if len(mylist) == 1:
        print(mylist[0])
        return

    print(mylist[0])
    show_seq(mylist[1:])

# main
list1 = [1,2,3,4,5,6]
show_seq(list1)