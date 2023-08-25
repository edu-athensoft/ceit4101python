"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data :
[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values:
{'S005', 'S002', 'S007', 'S001', 'S009'}


Hints:
nested in-line for-loop
set
dict.values()
"""


L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
     {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)

# u_value = set( val for dic in L for val in dic.values())
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

myset = set()
for dic in L:
    for val in dic.values():
        myset.add(val)
print(myset)
