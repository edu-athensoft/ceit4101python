# string
print('==== Data type : string ====')

str1 = 'abc'    # using quote
print(str1)

str2 = "abc"    # using double quote
print(str2)

str3 = "I'm ok" # mix
print(str3)

str4 = 'I\'m \"OK\"!'   # using escaped char
print(str4)

print() # blank line

# escaped characters
print('==== escaped characters ====')
esc_str1 = 'abc\ndef'     # new line \n
print(esc_str1)

esc_str2 = 'abc\tdef'     # tab \t
print(esc_str2)

esc_str3 = 'abc\\def'     # backslash \\
print(esc_str3)

esc_str4 = r'\\\t\\'     # escape the char sequence with r
print(esc_str4)

print()

# multiple line using ''' instead of \n
print('==== multiple line using \'\'\' instead of \\n')
str5 = '''line1:abc
line2:def
line3:ghi'''
print(str5)

print()

print('==== using r for multiple line')
print(r'''hello,\n
world''')