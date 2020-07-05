"""
define method in class

"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name}, {self.score}')

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


def main():
    stu1 = Student("Athens", 90)
    # print(stu1)

    stu1.print_score()
    print(stu1.get_grade())

    stu2 = Student("Lada", 80)
    # print(stu1)

    stu2.print_score()
    print(stu2.get_grade())


if __name__ == "__main__":
    main()
