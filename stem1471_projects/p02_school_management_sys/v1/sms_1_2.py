"""
project: school management system
version: 1

menu system - level 2

"""

print("school Management System")
print("ver 1.0")
print()


def viewAll():
    """ view student info list """
    print("viewAll()")


def viewById():
    """ view student info by Student ID """
    print("viewById()")


def viewByName():
    """ view student info by Student Name """
    print("viewByName()")


def create():
    """ create a new student record """
    print("create(studentRecord)")


def update():
    """ update a student record """
    print("update(studentRecord)")


def deleteById():
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
                update()
            elif option == '4':
                deleteById()
            else:
                print("[WARNING] Invalid option, please try again.")

            # continue or exit
            print("\nPress 'Enter' to continue or 'n' to exit:", end=" ")
            next_option = input().strip()
            if next_option == 'y' or next_option == "":
                print()
            else:
                print("Exiting system...")
                break


if __name__ == '__main__':
    main_start()
