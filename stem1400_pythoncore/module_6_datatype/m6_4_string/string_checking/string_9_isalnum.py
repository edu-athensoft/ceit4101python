"""
string method - isalnum()

returns True if all characters in the string are alphanumeric
If not, it returns False
"""

# invalid char = alphanumeric

while True:
    str1 = input("Enter your username: ")
    if str1.isalnum():
        print("Valid username.")
        break
    else:
        print("Invalid username.")

# not zero number -> True
# not empty string -> True
# None -> False
# 0 -> False
# empty string -> False

# while True
# while 1
# while 2
# while -1
# while 'abc'
# while ' '
# while '' -> False




