"""
Enrollment

=== Enrollment Service ===
Input your student ID:001
Input your first name:John
Input your last name:Smith
Input your grade number:G7
Input your email:j.smith@gmail.com
Input number of selected courses:4
"""

print("=== Enrollment Service ===")

# input info of student
# print("Input your student ID:", end="")
print("Input your student ID:")
student_id = input()

print("Input your first name:", end="")
first_name = input()

print("Input your last name:", end="")
last_name = input()

print("Input your grade number:", end="")
grade_number = input()

print("Input your email:", end="")
email = input()

print("Input number of selected courses:", end="")
num_courses = input()

# settings
CREDIT_PRICE = 50
CREDIT_PER_COURSE = 3

# processing
# calculating tuition fee
tuition_amount = int(num_courses) * CREDIT_PER_COURSE * CREDIT_PRICE
# print(tuition_amount)

print("Your tuition fee is $", float(tuition_amount), "CAD")
