"""
project: school management system
version: 1

menu system - level 1

"""

print("school Management System")
print("ver 1.0")
print()

# menu
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

        # continue or exit
        print("\nPress 'Enter' to continue or 'n' to exit:", end=" ")
        next_option = input()
        if next_option == 'y' or next_option == "":
            print()
        else:
            print("Exiting system...")
            break
