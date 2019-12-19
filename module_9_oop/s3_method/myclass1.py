# method
# class method

class Employee:

    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        Employee.num_of_emps +=1

    def get_fullname(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        pass


