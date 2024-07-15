"""
We need to figure out grades to the scores that students receive on exams. Please write a program to determine the grade for a given percentage score.
The rules are as following:
Score		Letter grade	Description
90-100		A+		Exceptional
80-89		A		Excellent
70-79		B		Good
60-69		C		Satisfactory
50-59		D		Barely acceptable
0-49		F		Unacceptable
"""

# Read the percentage score from the user
score = float(input("Enter the percentage score: "))

# Determine the grade and description
if 90 <= score <= 100:
    grade = "A+"
    description = "Exceptional"
elif 80 <= score < 90:
    grade = "A"
    description = "Excellent"
elif 70 <= score < 80:
    grade = "B"
    description = "Good"
elif 60 <= score < 70:
    grade = "C"
    description = "Satisfactory"
elif 50 <= score < 60:
    grade = "D"
    description = "Barely acceptable"
elif 0 <= score < 50:
    grade = "F"
    description = "Unacceptable"
else:
    grade = "Invalid"
    description = "Invalid score entered"

# Print the grade and description
print(f"Score: {score}\nGrade: {grade}\nDescription: {description}")
