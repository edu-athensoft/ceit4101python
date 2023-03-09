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

        """
        NameError: name 'score' is not defined
        because score is class variable and is being accessed in an instance method
        """
        # print(score)

        print("Worker.score in __init__ (via Class) ",Worker.score)


        # access class variable
        print("Worker.score in __init__ (via self.__class__)",self.__class__.score)

