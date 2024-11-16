def display_menu():
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")

def menu_loop():
    while True:
        display_menu()  # Show the menu options
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            print("You selected Option 1")
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("You selected Option 3")
        elif choice == '4':
            print("You selected Option 4")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

# Start the menu loop
menu_loop()
