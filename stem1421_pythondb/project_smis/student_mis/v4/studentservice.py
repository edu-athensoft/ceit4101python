"""
Service class of Student Business
"""

from studentdao import *
from viewtemplate import *


class StudentService:
    def __init__(self, database):
        self.studentDao = StudentDao(database)

    def close(self):
        try:
            self.studentDao.close()
            print("[DEBUG] StudentService has been closed.")
        except Exception as e:
            print("[ERROR] Error occurs when StudentService was closing.")

    @header
    @footer
    def viewAll(self):
        """ view student info list """
        results = self.studentDao.get_all()
        for student in results:
            print(TABLE_ROW_FORMAT.format(
                student.studentId,
                student.studentName,
                student.schoolName,
                student.gradeNo))

    @header
    @footer
    def viewById(self, id):
        """ view student info by Student ID """
        student = self.studentDao.get_by_id(id)
        if student:
            print(TABLE_ROW_FORMAT.format(
                student.studentId,
                student.studentName,
                student.schoolName,
                student.gradeNo))
        else:
            print("No results")

    @header
    @footer
    def viewByName(self, student_name):
        """ view student info by Student name """
        results = self.studentDao.get_by_studentname(student_name)
        if len(results):
            for student in results:
                print(TABLE_ROW_FORMAT.format(
                    student.studentId,
                    student.studentName,
                    student.schoolName,
                    student.gradeNo))
        else:
            print("No results")

    def create(self):
        """ create a new student record """
        print("Create a Student Record")
        print("Pattern: (StudentID, StudentName, SchoolName, GradeNo")
        print("Example: (1234, 'Bella', 'Saint Jean', 'G8')")

        def inputStudentRecord():
            while True:
                studentId = input("Student ID*:")
                if studentId:

                    # search student info by ID
                    studentRecord = self.studentDao.get_by_id(studentId)

                    if studentRecord:
                        print("[WARNING] Student: {studentID} already exists! ")
                        continue

                    break
                else:
                    print("Student ID is required. Please input again!")

            studentName = input("Student Name:")
            schoolName = input("School Name:")
            gradeNo = input("Grade No.:")

            studentObj = Student()
            studentObj.studentId = studentId
            studentObj.studentName = studentName
            studentObj.schoolName = schoolName
            studentObj.gradeNo = gradeNo
            return studentObj

        # input new student object
        student = inputStudentRecord()

        # save record, appending
        self.studentDao.create(student)
        # print summary
        print(f"[INFO] The Student Record {student} has been saved.")
        print()

    def update(self):
        """ update a student record by student ID"""
        print("Update a Student Record")

        # input student ID
        while True:
            studentID = input("Student ID* : ")
            if studentID:
                break
            else:
                print("[ERROR] Please input a valid student ID!")

        # search student info by ID
        studentObj = self.studentDao.get_by_id(studentID)

        if not studentObj:
            print("[WARNING] No such student record!")
            return
        else:
            print(f"Do you want to update {studentObj} ?")
            update_option = input("Press y to update and Enter to abort: ")
            if update_option.lower() == 'y':
                print("\nUpdate field with new value and press Enter to skip.")
                print(f"Student ID: {studentObj.studentId}")

                a = input("Student Name:").strip()
                studentObj.studentName = a if a != '' else studentObj.studentName

                b = input("School Name:").strip()
                studentObj.schoolName = b if b != '' else studentObj.schoolName

                c = input("Grade No:").strip()
                studentObj.gradeNo = c if c != '' else studentObj.gradeNo

                # test
                print(f"[DEBUG] studentObj={studentObj}")

                self.studentDao.update(studentObj)
                print(f"[INFO] Student Record has been changed to {studentObj}")
            else:
                return


    def deleteById(self):
        """ delete a student record by ID """
        print("Delete a Student Record")

        # input student ID
        while True:
            studentID = input("Student ID* : ")
            if studentID:
                break
            else:
                print("[ERROR] Please input a valid student ID!")

        # search student info by ID
        studentRecord = self.studentDao.get_by_id(studentID)

        if not studentRecord:
            print("[WARNING] No such student record!")
            return
        else:
            self.studentDao.delete_by_id(studentID)
            print(f"[INFO] The student record {studentRecord} has been deleted.")
        print()