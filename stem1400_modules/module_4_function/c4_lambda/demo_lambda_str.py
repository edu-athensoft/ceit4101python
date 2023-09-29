"""
demo

combine first name and last name
"""

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("Athens", "Zhang"))