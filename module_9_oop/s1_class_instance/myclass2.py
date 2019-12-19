# define a class
# create instance


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = "Athens"
emp1.last = "Zhang"
emp1.email = "athens314@hotmail.com"
emp1.pay = 90000


emp2.first = "Lada"
emp2.last = "Zhang"
emp2.email = "lada314@gmail.com"
emp2.pay = 96300
emp2.address = "emp2 address"

print(emp1.first)
print(emp2.email)
print(emp2.address)
# print(emp1.address)