"""
datetime module
Python format datetime
Python has strftime() and strptime() methods to handle this.

The strptime() method creates a datetime object
from a given string (representing date and time)

"""


from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object, type(date_object))
