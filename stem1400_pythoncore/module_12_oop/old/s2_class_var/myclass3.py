# class variable
# with raise_amount


class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def get_fullname(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Athens','Zhang','a1@163.com', 6000)
emp2 = Employee('Lada','Zhang','a2@263.com', 9000)

Employee.raise_amount = 1.04
print(emp1.raise_amount)
print(emp2.raise_amount)

