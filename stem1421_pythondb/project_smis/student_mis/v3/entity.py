"""
Entities
"""


class Student:
    def __init__(self, studentId, studentName, schoolName, gradeNo):
        self.studentId = studentId
        self.studentName = studentName
        self.schoolName = schoolName
        self.gradeNo = gradeNo

    def __str__(self):
        return f"Student ID: {self.studentId}, Name: {self.studentName}, School: {self.schoolName}, Grade: {self.gradeNo}"

    