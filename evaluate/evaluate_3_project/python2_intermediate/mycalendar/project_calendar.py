# Program to display calendar of the given month and year
# importing calendar module
import calendar

# yy = 2019  # year
# mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# display the calendar
# print(calendar.month(yy, mm))

# yy is set to 2019 as a default

def my_calendar(month, year=2019):
    print(calendar.month(year, month))

my_calendar(12)
my_calendar(1,2020)


# homework
# input year, print out 12 months of calendar





