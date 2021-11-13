"""
Client of LearningApp
"""

# test class variable
print("=== test class variable ===")
print(Student.name)
print(Student.age)


# test instance variables
print("=== test instance variables ===")
teacher1 = Teacher('Mr. Richel', 35)
print(teacher1.tname)
print(teacher1.age)

teacher2 = Teacher('Ms. Joce', 25)

print("=== before changed === ")
print("teacher1.lang",teacher1.lang)
print("teacher2.lang",teacher2.lang)


# changed class variable
print("=== after changed instance variable === ")
teacher1.lang = 'fr'
print("teacher1.lang",teacher1.lang)
print("teacher2.lang",teacher2.lang)

# changed class variable
print("=== after changed class variable === ")
Teacher.lang = 'cn'
print("teacher1.lang",teacher1.lang)
print("teacher2.lang",teacher2.lang)
