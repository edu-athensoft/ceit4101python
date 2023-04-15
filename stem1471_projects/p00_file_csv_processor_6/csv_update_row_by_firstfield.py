"""
csv file processor

In this example, we first define the value of the first field to search for.

We then open the CSV file in read mode and read the data into a
list of rows using the csv.reader object.

Next, we loop through the rows in the list using enumerate() to keep
track of the line number. We check each row to see if its first field
matches the search value. If we find a match, we use list indexing
to update the values in the row, and then break out of the loop.

Finally, we open the CSV file in write mode and write the updated
rows back to the file using the csv.writer object.

Note that we also specify newline='' when opening the file to
ensure that the correct line endings are used on all platforms.
"""

import csv

# define the value of the first field to search for
search_value = '3'

# open CSV file and read data into a list of rows
with open('data/input.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# loop through the rows to find the row with the matching value in the first field
for i, row in enumerate(rows):
    if row[0] == search_value:
        # update the values in the row
        rows[i][1] = 'new value for second column'
        rows[i][2] = 'new value for third column'
        break

# open CSV file in write mode and write updated rows back to the file
with open('data/output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)