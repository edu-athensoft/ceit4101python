"""
Find the 2nd index of the specified element in a given list in 3 ways
Given with [3, 8, 1, 6, 0, 8, 4], please find the position of the 2nd item of '8'

"""

numbers = [3, 8, 1, 6, 0, 8, 4, 8, 7, 8, 0]


def find(target, times=1):
    count = 1
    index = 0
    while count <= times and index < len(numbers):
        index1 = numbers[index:].index(target)
        print(index1+index)
        count += 1
        index = index1+index+1


def findall(target):
    count = 1
    index = 0
    while index < len(numbers):
        if target in numbers[index:]:
            index1 = numbers[index:].index(target)
            print(index1+index)
            count += 1
            index = index1+index+1
        else:
            break



# test
mytarget = 8
# find(mytarget)

# find(mytarget, 2)
# find(mytarget, 3)


findall(8)



