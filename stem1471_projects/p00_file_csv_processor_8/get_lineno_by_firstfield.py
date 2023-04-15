"""
get line no by first field
"""

import csv

search_value = '1'
search_value = '2'
line_number = None

with open('data/input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(reader):
        if row[0] == search_value:
            line_number = i + 1
            break

print(line_number)