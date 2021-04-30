"""
learning module

class variables
instance variables
"""


class Student:
    # class variables
    name = 'Noname'
    age = 0


class Teacher:
    lang = 'en'

    # instance variables
    def __init__(self, tname, age):
        self.tname = tname
        self.age = age


class Worker:
    score = 0

    def __init__(self, w_name, w_age):
        self.name = w_name
        self.age = w_age
        print("w_name",w_name)
        print("w_age",w_age)
        print("self.name",self.name)
        print("self.age",self.age)

        # self.__class__.score += 1

        # print("current Worker.score = "+str(self.__class__.score))

    # define a class method
    @classmethod
    def plus_score(cls):
        cls.score += 1
        print(cls.score)
