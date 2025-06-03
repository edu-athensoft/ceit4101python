import os


def safely_delete_file():
    file_name = input("Enter the name of the file you want to delete: ")

    if os.path.exists(file_name):
        try:
            os.remove(file_name)
        except PermissionError:
            print("Error")
        except Exception as e:
            print("Error")
    else:
        print("Error: The file '{file_name}' does not exist.")


safely_delete_file()