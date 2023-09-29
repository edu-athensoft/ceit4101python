"""
A test app for student entity
"""

import studentdb

"""
# add records

s1 = (1001, 'Peter', 'Saint Mary', 'G7')
studentdb.add(s1)

students = [
    (1002, 'Jack', 'Saint Queen', 'G8'),
    (1003, 'Tom', 'Saint Mary', 'G9'),
    (1004, 'Jerry', 'Saint Mary', 'G10')]
studentdb.add_many(students)
"""

"""
# update records

s2 = (1004, 'Jerry', 'Jean-de-Eudes', 'G9')
studentdb.update(s2)
"""

"""
# delete record by id
s5 = (1005, 'Lada', 'Saint Mary', 'G12')
studentdb.add(s5)
studentdb.delete(s5[0])
"""

"""
# retrieve records
"""
# select by id
stu_id = 1009
result = studentdb.get_by_id(stu_id)
print(result)

# select all
# results = studentdb.get_all()
# print(results)
