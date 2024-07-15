"""
We use 1 to 7 to represent days of week based on ISO weekday definitions.
Please write a program to print out the name of day of week by a given number from 1 to 7.
Hint: Using switch statement
Sample input:  1
Expected result: Monday

"""

# Sample input
day_number = int(input("Enter a number (1 to 7): "))

# Determine the day of the week
if day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"
elif day_number == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid day number"

# Print the result
print(day_name)