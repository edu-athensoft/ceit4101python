"""
Entities
"""


class Student:
    def __init__(self, studentId=None, studentName=None, schoolName=None, gradeNo=None):
        self.studentId = studentId
        self.studentName = studentName
        self.schoolName = schoolName
        self.gradeNo = gradeNo

    def __str__(self):
        return f"studentId: {self.studentId}, studentName: {self.studentName}, schoolName: {self.schoolName}, gradeNo: {self.gradeNo}"
