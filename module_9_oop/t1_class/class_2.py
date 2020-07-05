# -*- coding: utf-8 -*-
"""
attributes of object

"""


class Student(object):
    pass


def main():

    # object 1
    stu1 = Student()
    print(stu1)

    # object attributes
    stu1.name = "Jovy"
    stu1.grade = "G7"
    print(stu1.name)
    print(stu1.grade)

    # object 2
    stu2 = Student()
    print(stu2)

    # object attributes
    print(stu2.name)
    print(stu2.grade)


if __name__ == "__main__":
    main()
