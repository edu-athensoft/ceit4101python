# sorted()

# sorted(iterable[, key][, reverse])

# sorted() Parameters
# sorted() takes two three parameters:
#
# iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator
# reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
# key (Optional) - function that serves as a key for the sort comparison


# Return value from sorted()
# sorted() method returns a sorted list from the given iterable.




# Sort a given sequence: string, list and tuple
# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string
pyString = 'Python'
print(sorted(pyString))

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))



# Sort a given collection in descending order: set, dictionary and frozen set
# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(pyDict, reverse=True))

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(pyFSet, reverse=True))



# Sort the list using sorted() having a key function
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)