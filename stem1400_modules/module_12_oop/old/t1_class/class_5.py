"""
define method in class

"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name}, {self.score}')


def main():
    stu1 = Student("Athens", 90)
    print(stu1)

    stu1.print_score()


if __name__ == "__main__":
    main()
