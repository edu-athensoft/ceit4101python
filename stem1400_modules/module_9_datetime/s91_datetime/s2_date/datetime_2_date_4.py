"""
datetime module
date class
datetime.date

The range of month
The range of day

"""

from datetime import date

# month ranges from 1 to 12
d = date(2015, 1, 30)
print(d)
# d = date(2015, 0, 30)
# d = date(2015, 13, 30)
# ValueError: month must be in 1..12
print()

# day ranges according to the valid month given
d = date(2015, 1, 31)
print(d)

# d = date(2015, 1, 0)
# d = date(2015, 1, 32)
# print(d)


d = date(2015, 2, 29)
# print(d)

# ValueError: day is out of range for month



