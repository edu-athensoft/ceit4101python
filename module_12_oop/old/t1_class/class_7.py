"""
private property
mutator
"""


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print(f'{self.__name}, {self.__score}')

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


def main():
    stu1 = Student("Athens", 90)
    # stu1.print_score()

    print(stu1.get_name())
    print(stu1.get_score())
    print()

    stu1.set_name("Lada")
    stu1.set_score(80)

    print(stu1.get_name())
    print(stu1.get_score())


if __name__ == "__main__":
    main()
