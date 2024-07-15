"""
Please write a menu for a CLI (command line interface) application to present options like list all records, create a new record, update a record, delete a record and quit.
Hint: Using if-statement
Sample Output:
1. list all records
2. create a new record
3. update a record
4. delete a record
5. quit

User Input:  4
You selected 'delete a record'

"""
# Print the menu options
print("Menu:")
print("1. List all records")
print("2. Create a new record")
print("3. Update a record")
print("4. Delete a record")
print("5. Quit")

# Read user input
choice = input("Enter your choice (1-5): ")

# Handle the user input
if choice == "1":
    print("You selected 'list all records'")
    # Add code to list all records here
elif choice == "2":
    print("You selected 'create a new record'")
    # Add code to create a new record here
elif choice == "3":
    print("You selected 'update a record'")
    # Add code to update a record here
elif choice == "4":
    print("You selected 'delete a record'")
    # Add code to delete a record here
elif choice == "5":
    print("You selected 'quit'")
    print("Goodbye!")
else:
    print("Invalid choice, please enter a number between 1 and 5.")