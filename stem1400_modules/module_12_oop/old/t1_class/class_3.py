# -*- coding: utf-8 -*-

"""
constructor
attributes of class
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


def main():

    # error
    # stu1 = Student()
    # print(stu1)

    # correct
    stu2 = Student("Athens", 90)
    print(stu2)

    print(stu2.name)
    print(stu2.score)


if __name__ == "__main__":
    main()

