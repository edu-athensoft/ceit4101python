#
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        # pass
        cls.raise_amt = amount


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Tester', 'Employee', 60000)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
print()

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

print(emp1.__dict__)