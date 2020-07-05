"""
access from outer function
"""

from module_9_oop.t1_class.class_3 import Student


def print_score(stu):
    print(f'Student: name = {stu.name}, score = {stu.score}')


s = Student("Athens",90)
print_score(s)

