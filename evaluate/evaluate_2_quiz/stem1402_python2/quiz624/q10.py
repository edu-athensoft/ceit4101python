"""
10. Write a Python function remove_all_occurrences(mylist, element) that takes a list mylist and an element element as parameters. The function should remove all occurrences of element from mylist. After removing all occurrences of element, the function should return the modified list. You should also ensure that the original list order is preserved.
Input:
mylist = ['apple', 'banana', 'cherry', 'banana'], element = 'banana'
Output:
['apple', 'cherry']

Input:
mylist = [1, 2, 3, 4, 5], element = 6
Output:
[1, 2, 3, 4, 5] (Since 6 is not in the list, the list is returned unchanged.)

"""


# without list APIs and built-in functions

def remove_all_occurrences(mylist: list, element) -> list:

    if element not in mylist:
        return mylist

    result = []
    for item in mylist:
        if item == element:
            continue
        result.append(item)
    return result


list1 = ['apple', 'banana', 'cherry', 'banana']
element1 = 'banana'

result_list = remove_all_occurrences(list1, element1)
print(result_list)
