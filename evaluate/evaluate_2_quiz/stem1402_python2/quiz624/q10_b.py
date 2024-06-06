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


# through list APIs or built-in functions
list1 = ['apple', 'banana', 'cherry', 'banana']
element1 = 'banana'

result_list = list(filter(lambda x: x != 'banana', list1))
print(result_list)
