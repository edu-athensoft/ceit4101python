"""
Quiz 313
q5

In Canada, the age ranges for different stages of life are
not strictly defined and can vary depending on factors such
as culture and lifestyle. However, generally speaking, people
under the age of 14 are often referred to as 'children', and
people who are between the ages of 14 to 17 are referred to
"youth", while people between the ages of 18 to 24 are often
referred to as "young adults", while those between the ages
of 25 to 64 are considered "working-age adults". People aged 65
and over are generally referred to as "seniors" or "older adults".

Please write a program to tell what a person can be called
by range of age with a specified number of age.
Hint:	Please save your code in the file naming as stem1401_quiz313_q5_yourname.py
"""

"""
children            age < 14
youth               14 <= age <= 17
young adults        18 <= age <= 24
working-age adults  25 <= age <= 64
seniors             age >= 65
"""

print("=== TITLE GOES HERE ===")

age = int(input("Please input a number of age: "))
# we may check age if it is valid here
# sys.exit("Values do not match")
# quit()
# exit()

if age <= 0:
    print("Invalid input!")
    exit()

class_name_by_age = "Unknown"

if age < 14:
    class_name_by_age = "children"
elif 14 <= age <= 17:
    class_name_by_age = "youth"
elif 18 <= age <= 24:
    class_name_by_age = "young adults"
elif 25 <= age <= 64:
    class_name_by_age = "working-age adults"
elif age >= 65:
    class_name_by_age = "seniors"
else:
    # print("Invalid input")
    pass

print(class_name_by_age)
