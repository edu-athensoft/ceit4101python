"""
password generator
"""

import string
import random


def get_valid_chars():
    LETTERS = string.ascii_letters

    DIGITS = string.digits

    SYMBOLS = string.punctuation

    # removing quote, and double quote
    SYMBOLS = SYMBOLS.replace('\'', '')
    SYMBOLS = SYMBOLS.replace('\"', '')

    return LETTERS + DIGITS + SYMBOLS


def generate_pwd(length_of_pwd=8):
    charset = get_valid_chars()
    pwd = ''
    for i in range(length_of_pwd):
        pwd += random.choice(charset)
    return pwd

# main
# print(get_valid_chars())

pwd_length = 12

print(generate_pwd(pwd_length))
print(generate_pwd(pwd_length))
print(generate_pwd(pwd_length))
print(generate_pwd(pwd_length))
print(generate_pwd(pwd_length))
