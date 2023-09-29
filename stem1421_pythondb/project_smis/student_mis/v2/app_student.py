"""
Application
Client of student
"""

from studentdao import *

from mydbutil import *

print("School Management System")
print("Ver 1.0")
print()


def viewAll():
    """ view student info list """
    print("{:^66}".format(" Student Info "))
    print("-" * 66)
    print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
    print("-" * 66)

    results = studentDao.get_all()
    for student in results:
        print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                  student.gradeNo))
    print("-" * 66)
    print()


def viewById(id):
    """ view student info by Student ID """
    print("viewById()", file=open('log.txt', 'a'))

    print("{:^66}".format(" Student Info "))
    print("-" * 66)
    print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
    print("-" * 66)

    student = studentDao.get_by_id(id)
    if student:
        print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                  student.gradeNo))
    else:
        print("No such record")
    print("-" * 66)
    print()


def viewByName(student_name):
    """ view student info by Student name """
    print("viewById()", file=open('log.txt', 'a'))

    print("{:^66}".format(" Student Info "))
    print("-" * 66)
    print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
    print("-" * 66)

    results = studentDao.get_by_studentname(student_name)
    if len(results):
        for student in results:
            print("{:^10}  {:16}   {:28}{:^6}".format(student.studentId, student.studentName, student.schoolName,
                                                      student.gradeNo))
    else:
        print("No such record")
    print("-" * 66)
    print()


def create():
    """ create a new student record """
    print("Create a Student Record")
    print("Pattern: (StudentID, StudentName, SchoolName, GradeNo")
    print("Example: (1234, 'Bella', 'Saint Jean', 'G8')")

    def inputStudentRecord():
        while True:
            studentID = input("Student ID*:")
            if studentID:

                # search student info by ID
                studentRecord = studentDao.get_by_id(studentID)

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


def update():
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
    studentRecord = studentDao.get_by_id(studentID)

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


def deleteById():
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
    studentRecord = studentDao.get_by_id(studentID)

    if not studentRecord:
        print("[WARNING] No such student record!")
        return
    else:
        studentDao.delete_by_id(studentID)
        print(f"The student record {studentRecord} has been deleted.")
    print()


# main
studentDao = StudentDao(get_connection("smis"))


def main_start():
    while True:
        # print menu level 1
        print("======== Main menu ========")
        print(" 1. View student Info list")
        print(" 2. Create student record")
        print(" 3. Update student record")
        print(" 4. Delete student record")
        print(" 0. Exit")
        print("===========================")
        option = input("Please choose your option: ")

        if option == '0':
            print("Exiting system...")
            break
        else:
            # nav to selected option of level 2
            if option == '1':
                while True:
                    # print menu level 2
                    print("  View or Search Student Records: ")
                    print("  1. View all students")
                    print("  2. Search student by id")
                    print("  3. Search student by name")
                    print("  0. Return to Main Menu")
                    option2 = input("  Choose option: [1-3,0] ")
                    if option2 == '0':
                        print()
                        break
                    elif option2 == '1':
                        viewAll()
                    elif option2 == '2':
                        print("    Enter student id:", end="")
                        student_id = input()
                        viewById(student_id)
                    elif option2 == '3':
                        print("    Enter student name:", end="")
                        student_name = input()
                        viewByName(student_name)
                    else:
                        print()

            elif option == '2':
                create()
            elif option == '3':
                update()
            elif option == '4':
                deleteById()
            else:
                print("[WARNING] Invalid option, please try again.")


if __name__ == '__main__':
    main_start()
