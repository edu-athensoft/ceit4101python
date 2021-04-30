"""
interpolation search

"""
def formula(l, r, key, array):
    p = (key - array[l]) / (array[r] - array[l])
    n = r - l
    idx = int(n * p)
    return idx


def interpolation_search(array, key):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + formula(left, right, key, array)
        if array[mid] == key:
            return mid  # success
        elif array[mid] < key:
            left = mid + 1  # search in the right part
        else:
            right = mid - 1  # search in the left part
    return -1  # fail


# main program
# case 1.
myarr = [1,3,5,7,9,11,13,15,17,19]

# the first attempt
key = 13
res = interpolation_search(myarr, key)
print(f"The position of key:{key} is at the index of {res}")

# the second attempt
key = 9
res = interpolation_search(myarr, key)
print(f"The position of key:{key} is at the index of {res}")

# the second attempt
key = 10
res = interpolation_search(myarr, key)
print(f"The position of key:{key} is at the index of {res}")


# case 2.
myarr2 = [1,3,5,7,8,11,13,15,18,19]

# the first attempt
key = 8
res = interpolation_search(myarr2, key)
print(f"The position of key:{key} is at the index of {res}")

# the second attempt
key = 18
res = interpolation_search(myarr2, key)
print(f"The position of key:{key} is at the index of {res}")
