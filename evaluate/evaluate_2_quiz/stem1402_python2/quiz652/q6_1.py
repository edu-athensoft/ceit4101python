"""
quiz 652
6. Write a program to add one or more members to a set at a time
Hints: update()
"""


def main():
    my_set = set()
    print("Initial set:", my_set)

    while True:
        user_input = input("Enter an element or multiple elements separated by commas (type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        # Check if the input contains multiple elements separated by commas
        if ',' in user_input:
            # Split the string by commas and strip spaces, then add elements using update()
            elements = [element.strip() for element in user_input.split(',')]
            my_set.update(elements)
        else:
            # Add a single element using add()
            my_set.add(user_input.strip())

        print("Updated set:", my_set)


if __name__ == "__main__":
    main()