"""
csv processor

append a row

In this example, we first define the data that we want to
append to the CSV file, which is a list of values representing
a new row of data.

We then open the CSV file in append mode by specifying 'a'
as the file mode. This allows us to append data to the end of
the file rather than overwriting the entire file.

Finally, we use the csv.writer object to write the new row of
data to the CSV file using the writerow() method.

Note that we also specify newline='' when opening the file to
ensure that the correct line endings are used on all platforms.
"""

import csv

# data to append to CSV file
new_row = [6, 'Cathy', 'Saint Luc', 'G8']

# open CSV file in append mode
with open('data/output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_row)



