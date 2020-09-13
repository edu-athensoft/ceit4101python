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
Python file method readline()reads one entire line from the file. 
A trailing newline character is kept in the string. 
If the size argument is present and non-negative, 
it is a maximum byte count including the trailing newline 
and an incomplete line may be returned.

An empty string is returned only 
when EOF is encountered immediately.

The readline() method returns one line from the file.

You can also specified how many bytes from the line to return, 
by using the size parameter.
"""


"""
return "" when reach EOF
"""

f = open("file5_mode_r.txt",'r')

# readline
# read the first line
line = f.readline()
print(line)

# read next line
line = f.readline()
print(line)


# read by size
line = f.readline(3)
print(line)

f.close()

