"""
csv file processor

delete row(s) by line no.

In this example, we first open the CSV file in read mode
and read the data into a list of rows using the csv.reader object.

We then define the line number of the row that we want to delete.

Next, we use the pop() method to remove the row at the specified
line number from the list of rows. We subtract 1 from the line number
because lists in Python are zero-indexed.

Finally, we open the CSV file in write mode and write the remaining
rows back to the file using the csv.writer object.

Note that we also specify newline='' when opening the file to ensure
that the correct line endings are used on all platforms.
"""

import csv

# open CSV file and read data into a list of rows
with open('data/input.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# define the line number of the row to delete
line_number = 2

# remove the row from the list of rows
deleted_row = rows.pop(line_number - 1)

# open CSV file in write mode and write remaining rows back to the file
with open('data/output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
