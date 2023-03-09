"""
built-in error
EOFError

press Ctrl+D to generate an EOFError
"""

# n = int(input())
# print(n * 5)


try:
    n = int(input())
    print(n * 5)

except EOFError as e:
    print(e)

# EOF when reading a line
