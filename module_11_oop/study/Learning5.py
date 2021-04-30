"""
learning module

static method
class method

"""


class Worker:
    score = 0

    def __init__(self, w_name, w_age):
        self.name = w_name
        self.age = w_age
        print("w_name",w_name)
        print("w_age",w_age)
        print("self.name",self.name)
        print("self.age",self.age)

    # define a class method
    @classmethod
    def plus_score(cls):
        cls.score += 1
        print(cls.score)

    @staticmethod
    def add(x, y):
        print(Worker.score)
        print('This is a static method')
