"""
Application
Client of student
"""

from studentservice import *


def view_all_student():
    print()
    studentService.viewAll()


def view_student_by_id():
    print("  Enter student id: ", end="")
    student_id = input()
    print()
    studentService.viewById(student_id)


def view_student_by_name():
    print("  Enter student name: ", end="")
    student_name = input()
    print()
    studentService.viewByName(student_name)


def create_student():
    studentService.create()


def update_student():
    studentService.update()
    print()


def delete_student():
    studentService.deleteById()
    print()


def no_action():
    print()


def main_start():
    print("School Management System")
    print("Ver 1.0")
    print()

    while True:
        # menu level 1
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
            # menu level 2
            if option == '1':
                while True:
                    # print menu level 2
                    print("  View or Search Student Records: ")
                    print("  1. View all students")
                    print("  2. Search student by id")
                    print("  3. Search student by name")
                    print("  0. Return to Main Menu")
                    print("-----------------------------")
                    option2 = input("  Choose option: [1-3,0] ")

                    if option2 == '0':
                        no_action()
                        break
                    elif option2 == '1':
                        view_all_student()
                    elif option2 == '2':
                        view_student_by_id()
                    elif option2 == '3':
                        view_student_by_name()
                    else:
                        no_action()

            elif option == '2':
                create_student()
            elif option == '3':
                update_student()
            elif option == '4':
                delete_student()
            else:
                print("[WARNING] Invalid option, please try again.")


# main
if __name__ == '__main__':
    DB_NAME = "smis"
    DB_HOST = '192.168.1.16'
    studentService = StudentService(database=DB_NAME, dbhost=DB_HOST)
    main_start()
    studentService.close()
