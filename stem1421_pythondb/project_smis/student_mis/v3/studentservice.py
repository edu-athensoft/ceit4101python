"""
Service class of Student Business
"""

from studentdao import *


class StudentService:
    def __init__(self, database):
        self.studentDao = StudentDao(database)

    def close(self):
        try:
            self.studentDao.close()
            print("[INFO] StudentService has been closed.")
        except Exception as e:
            print("[ERROR] Error occurs when StudentService was closing.")


    def viewAll(self):
        """ view student info list """
        print("{:^66}".format(" Student Info "))
        print("-" * 66)
        print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
        print("-" * 66)

        results = self.studentDao.get_all()
        for student in results:
            print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                      student.gradeNo))
        print("-" * 66)
        print()


    def viewById(self, id):
        """ view student info by Student ID """
        print("viewById()", file=open('log.txt', 'a'))

        print("{:^66}".format(" Student Info "))
        print("-" * 66)
        print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
        print("-" * 66)

        student = self.studentDao.get_by_id(id)
        if student:
            print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                      student.gradeNo))
        else:
            print("No such record")
        print("-" * 66)
        print()


    def viewByName(self, student_name):
        """ view student info by Student name """
        print("viewById()", file=open('log.txt', 'a'))

        print("{:^66}".format(" Student Info "))
        print("-" * 66)
        print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
        print("-" * 66)

        results = self.studentDao.get_by_studentname(student_name)
        if len(results):
            for student in results:
                print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                          student.gradeNo))
        else:
            print("No such record")
        print("-" * 66)
        print()


    def create(self):
        """ create a new student record """
        print("Create a Student Record")
        print("Pattern: (StudentID, StudentName, SchoolName, GradeNo")
        print("Example: (1234, 'Bella', 'Saint Jean', 'G8')")

        def inputStudentRecord():
            while True:
                studentID = input("Student ID*:")
                if studentID:

                    # search student info by ID
                    studentRecord = self.studentDao.get_by_id(studentID)

                    if studentRecord:
                        print("[WARNING] Student: {studentID} already exists! ")
                        continue

                    break
                else:
                    print("Student ID is required. Please input again!")

            studentName = input("Student Name:")
            schoolName = input("School Name:")
            gradeNo = input("Grade No.:")

            new_row = []
            new_row.append(studentID)
            new_row.append(studentName)
            new_row.append(schoolName)
            new_row.append(gradeNo)
            return new_row

        # input new row
        new_row = inputStudentRecord()

        # save record, appending
        StudentDao.create(new_row)
        # print summary
        print(f"The Student Record {tuple(new_row)} has been saved.")
        print()


    def update(self):
        """ update a student record by student ID"""
        print("update(studentRecord)\n")

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
            studentRecord = list(studentRecord)
            print(f"Do you want to update {studentRecord} ?")
            update_option = input("Press y to update and Enter to abort: ")
            if update_option.lower() == 'y':
                print("\nUpdate field with new value and press Enter to skip.")
                print(f"Student ID: {studentRecord[0]}")

                a = input("Student Name:").strip()
                studentRecord[1] = a if a != '' else studentRecord[1]

                b = input("School Name:").strip()
                studentRecord[2] = b if b != '' else studentRecord[2]

                c = input("Grade No:").strip()
                studentRecord[3] = c if c != '' else studentRecord[3]

                StudentDao.update(studentRecord)
                print(f"Student Record has been changed to {studentRecord}")
            else:
                return


    def deleteById(self):
        """ delete a student record by ID """
        print("deleteById(studentId)")

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
            print(f"The student record {studentRecord} has been deleted.")
        print()