"""
project: school management system
version: 1

implement viewAll() function

"""

import csv

print("school Management System")
print("ver 1.0")
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


def update(studentRecord):
    """ update a student record """
    print("update(studentRecord)")


def deleteById(studentId):
    """ delete a student record by ID """
    print("deleteById(studentId)")


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
            print(f"Option: {option}")
            # route to selected option of level 2
            if option == '1':
                viewAll()
            elif option == '2':
                create()
            elif option == '3':
                update([])
            elif option == '4':
                deleteById(1)
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
