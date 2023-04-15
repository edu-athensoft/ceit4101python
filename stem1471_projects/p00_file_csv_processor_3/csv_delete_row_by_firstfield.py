"""
csv file processor

delete row(s) by first field with specified value

In this example, we first open the CSV file in read mode and read the data into a list of rows using the csv.reader object.

We then define the value that we want to search for in the first field of each row.

Next, we use a list comprehension to filter out the rows that match the search value in the first field. The filtered rows are stored in a new list called filtered_rows.

Finally, we open the CSV file in write mode and write the filtered rows back to the file using the csv.writer object.

Note that we also specify newline='' when opening the file to ensure that the correct line endings are used on all platforms.
"""

import csv

# open CSV file and read data into a list of rows
with open('data/output.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# define the value to search for in the first field
search_value = '4'

# filter out rows that match the search value in the first field
filtered_rows = [row for row in rows if row[0] != search_value]

# open CSV file in write mode and write filtered rows back to the file
with open('data/output_new.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_rows)