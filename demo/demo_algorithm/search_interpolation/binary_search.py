"""
binary search

"""


# if found, return the index(position) of x in the array 'arr'
# if not found, return -1
def binary_search(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)

        # found
        if arr[mid] == x:
            return mid

        # search in the left part
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # search in the right part
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # not exist
        return -1


# main program
arr = [2, 3, 4, 10, 40]


# first attempt
key = 10
res = binary_search(arr, 0, len(arr) - 1, key)

if res != -1:
    print(f"The element of {key} is at the index of {res}")
else:
    print(f"The element of {key} does not exist in the array")


# second attempt
key = 11
res = binary_search(arr, 0, len(arr) - 1, key)

if res != -1:
    print(f"The element of {key} is at the index of {res}")
else:
    print(f"The element of {key} does not exist in the array")
