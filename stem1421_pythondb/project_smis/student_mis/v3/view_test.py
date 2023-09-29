"""
Test template of table
Test view
"""


def header(func):
    def wrapper(*args, **kwargs):
        print("===header===")
        func(*args, **kwargs)

    return wrapper


def footer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("===footer===")

    return wrapper


@header
@footer
def show_table():
    print("Table data")


show_table()
