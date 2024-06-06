"""
5. Write a program to find all indices of target elements in a list.
my_list = [3, 8, 1, 6, 0, 8, 4, 8, 9, 8]

"""


def find_indices(mylist, target, start=0, found_indices=None):
    if found_indices is None:
        found_indices = []

    try:
        # start searching from beginning for element
        index = mylist.index(target, start)
        # when found, add index to found_indices
        found_indices.append(index)
        # recursively find from next position
        find_indices(mylist, target, index + 1, found_indices)
    except ValueError:
        # stop when no more element found
        pass

    return found_indices


# test
lst = [3, 8, 1, 6, 0, 8, 4, 8, 9, 8]
# target
element = 8
# find
indices = find_indices(lst, element)
print(indices)
