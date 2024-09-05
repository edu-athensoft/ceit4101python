# define a class
# user custom method


class Employee:
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def get_fullname(self):
        print('{} {}'.format(self.first, self.last))


emp1 = Employee('Athens','Zhang','a1@163.com', 6000)
emp2 = Employee('Lada','Zhang','a2@263.com', 9000)

emp1.get_fullname()
emp2.get_fullname()
