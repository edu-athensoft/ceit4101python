"""
Mode	Description
'r'	    Open a file for reading. (default)
'w'	    Open a file for writing.
        Creates a new file if it does not exist or truncates the file if it exists.
'x'	    Open a file for exclusive creation.
        If the file already exists, the operation fails.
'a'	    Open for appending at the end of the file without truncating it.
        Creates a new file if it does not exist.
't'	    Open in text mode. (default)
'b'	    Open in binary mode.
'+'	    Open a file for updating (reading and writing)
"""

"""
readlines
"""


f = open("file5_mode_r.txt", 'r')

# readlines
# read the first line
a = f.readlines()

print(a, type(a))
for i in a:
    print(i, end='')

f.close()

