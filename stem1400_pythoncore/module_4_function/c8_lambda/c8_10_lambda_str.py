"""
demo

concatenate first name and last name into a full name
"""

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("athens", "zhang"))
