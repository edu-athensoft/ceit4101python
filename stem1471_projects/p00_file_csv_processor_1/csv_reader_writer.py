"""
csv file processor
reader
writer

In this example, we use the csv module in Python to read data
from an input CSV file named "input.csv". We then manipulate
the data by appending a new value to each row. Finally, we use
the same csv module to write the updated data to an output
CSV file named "output.csv".

The with statement is used to ensure that the files are properly
closed after reading and writing, even if an exception occurs.
The newline='' parameter is used when opening the output CSV file
to ensure that the file is written with the correct line endings
on all platforms.
"""

import csv

# Read data from CSV file
with open('data/input.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Manipulate data
for row in data:
    row.append('new value')

# Write data to CSV file
with open('data/output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
