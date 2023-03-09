"""
string method - strip()

returns a copy of the string by removing both the leading and the trailing characters
"""

# case 1.
s = '  xoxo python xoxo  '

print(f"|{s}|")
print(f"|{s.strip()}|")

# case 2.
s = '  xoxo python xoxo  '
print(f"|{s}|")
print(f"|{s.strip('xo')}|")
print(f"|{s.strip('  xo')}|")
s = '  oxoxoxoab python abxoxoxoo  '
print(f"|{s.strip('  xo')}|")

# case 3.
s = 'android is awesome'
print(f"|{s.strip('an')}|")

# application
name = input("Enter your name:")
print(f"|{name}|")

if name.strip() == 'peter':
# if name == 'peter':
    print("correct username!")
else:
    print("incorrect!")
