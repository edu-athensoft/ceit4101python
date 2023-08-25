"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

# Loading the lowercase alphabet to a list
import string

# get alphabet
alphabet = set(string.ascii_lowercase)
print(alphabet)

# get user input

target = 'This is my lazy father who broken a very expensive glass jar which had been standing there quietly for long time.'
target = 'The quick brown fox jumps over the lazy dog'
target = 'The book is expensive but I like it.'

# preprocessing
# to lowercase
lower_target = target.lower()
print(lower_target)

isPangram = alphabet.issubset(lower_target)
print(isPangram)


