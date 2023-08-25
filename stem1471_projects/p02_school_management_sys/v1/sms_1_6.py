"""
project: school management system
version: 1

implement update() function

"""

import csv

print("School Management System")
print("Ver 1.0")
print()


def viewAll():
    """ view student info list """
    print("viewAll()")

    print("{:^66}".format(" Student Info "))
    print("-" * 66)
    print("{:^9}{:^16}{:^28}{:^15}".format("Student ID", "Student Name", "School Name", "Grade No."))
    print("-" * 66)
    with open('data/student_info.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print("{:^10}  {:16}   {:28}{:^6}".format(row[0], row[1], row[2], row[3]))


def viewById():
    """ view student info by Student ID """
    print("viewById()")


def viewByName():
    """ view student info by Student Name """
    print("viewByName()")


def searchById(studentId):
    search_value = studentId
    row_number = None

    with open('data/student_info.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            if row[0].strip() == search_value:
                row_number = i
                break

    if row_number is None:
        row = None
    return row_number, row


def create():
    """ create a new student record """
    print("create(studentRecord)")

    def inputStudentRecord():
        # new_row = [1, 'Cathy', 'Saint Luc', 'G8']
        new_row = []

        while True:
            studentID = input("Student ID*:")
            if studentID:
                break
            else:
                print("Student ID is required. Please input again!")

        studentName = input("Student Name:")
        schoolName = input("School Name:")
        gradeNo = input("Grade No.:")

        new_row.append(studentID)
        new_row.append(studentName)
        new_row.append(schoolName)
        new_row.append(gradeNo)
        return new_row

    # input new row
    new_row = inputStudentRecord()

    # save record, appending
    with open('data/student_info.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

    # print summary
    print(f"The student info {new_row} has been saved.")


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
    row_no, studentRecord = searchById(studentID)

    # print(">>>",row_no, studentRecord)

    def update_record(row_no, updated_row):
        with open('data/student_info.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # line no
        rowIndex = row_no

        # modify the values in the row
        rows[rowIndex] = updated_row

        # open CSV file in write mode and write updated rows back to the file
        with open('data/student_info.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    if not studentID:
        print("[WARNING] No such student record!")
        return

    if studentID:
        print(f"Do you want to update {studentRecord} ?")
        update_option = input("Press y to update and Enter to abort: ")
        if update_option.lower() == 'y':
            print("\nUpdate field with new value and press Enter to skip.")
            print(f"Student ID: {studentRecord[0]}")

            a = input("Student Name:").strip()
            studentRecord[1] =  a if a!='' else studentRecord[1]

            b = input("School Name:").strip()
            studentRecord[2] =  b if b!='' else studentRecord[2]

            c = input("Grade No:").strip()
            studentRecord[3] = c if c!='' else studentRecord[3]

            update_record(row_no, studentRecord)
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

    row_number, row  = searchById(studentID)
    if row_number is None:
        print("[WARNING] No such student record! Deletion aborted.")
        return

    # open CSV file and read data into a list of rows
    with open('data/student_info.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # remove the row from the list of rows
    deleted_row = rows.pop(row_number)

    # open CSV file in write mode and write remaining rows back to the file
    with open('data/student_info.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"The row {row} has been deleted.")


# main
def main_start():
    while True:
        # print menu level 1
        print("======== Main menu ========")
        print("1. View student Info list")
        print("2. Create student record")
        print("3. Update student record")
        print("4. Delete student record")
        print("0. Exit")
        print("===========================")
        option = input("Please choose your option: ")

        if option == '0':
            print("Exiting system...")
            break
        else:
            # print(f"Option: {option}")
            # route to selected option of level 2
            if option == '1':
                viewAll()
            elif option == '2':
                create()
            elif option == '3':
                update()
            elif option == '4':
                deleteById()
            else:
                print("[WARNING] Invalid option, please try again.")

            # continue or exit
            print("\nPress 'Enter' to continue or 'n' to exit:", end=" ")
            next_option = input()
            if next_option == 'y' or next_option == "":
                print()
            else:
                print("Exiting system...")
                break


if __name__ == '__main__':
    main_start()
