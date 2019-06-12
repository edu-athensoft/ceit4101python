# define a class
# create instance


class Employee:
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay


emp1 = Employee('Athens','Zhang','a1@163.com', 6000)
emp2 = Employee('Lada','Zhang','a2@263.com', 9000)

print(emp1)
print(emp2)

print('{} {}'.format(emp1.first, emp1.last))
print('{} {}'.format(emp2.first, emp2.last))
