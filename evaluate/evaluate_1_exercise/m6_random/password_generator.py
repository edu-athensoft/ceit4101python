"""
password generator
"""

import string

LETTERS = string.ascii_letters
print(LETTERS)

DIGITS = string.digits
print(DIGITS)

SYMBOLS = string.punctuation
print(SYMBOLS)

# removing quote, and double quote
SYMBOLS = SYMBOLS.replace('\'', '')
SYMBOLS = SYMBOLS.replace('\"', '')
print(SYMBOLS)




