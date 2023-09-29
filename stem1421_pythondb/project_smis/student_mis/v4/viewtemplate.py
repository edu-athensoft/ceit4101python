"""
View template
Formatting data table
"""

# settings
TABLE_ROW_FORMAT = "{:^10}  {:16}   {:28}{:^6}"
TABLE_TITLE_FORMAT = "{:^66}"
TABLE_HEADER_FORMAT = "{:^9}{:^16}{:^28}{:^15}"
TABLE_SEPARATOR_1_FORMAT = "-" * 66
TABLE_SEPARATOR_2_FORMAT = "=" * 66
BLANK_FORMAT = ""


def header(func):
    def wrapper(*args, **kwargs):
        print(TABLE_SEPARATOR_2_FORMAT)
        print(TABLE_TITLE_FORMAT.format(" Student Information "))
        print(TABLE_SEPARATOR_1_FORMAT)
        print(TABLE_HEADER_FORMAT.format("Student ID", "Student Name", "School Name", "Grade No."))
        print(TABLE_SEPARATOR_1_FORMAT)

        func(*args, **kwargs)

    return wrapper


def footer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

        print(TABLE_SEPARATOR_2_FORMAT)
        print(BLANK_FORMAT)

    return wrapper
