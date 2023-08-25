# class variable
# without raise_amount


class Employee:
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def get_fullname(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * 1.05)

emp1 = Employee('Athens','Zhang','a1@163.com', 6000)
emp2 = Employee('Lada','Zhang','a2@263.com', 9000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

