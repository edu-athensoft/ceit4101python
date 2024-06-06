"""
remove()

Please write a program to remove all whitespace ' '  in a given string.
Hints:
Users are allowed to input a string (or a sentence) at a time from a keyboard.
"""

my_str = "abc abc aaa"
my_str = list(my_str)

LETTER = ' '
while LETTER in my_str:
    my_str.remove(LETTER)

print(my_str)
