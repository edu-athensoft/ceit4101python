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

# demo


with open('file9_mode_plus2.txt', 'w+') as f:
    # Note that f has now been truncated to 0 bytes, so you'll only
    # be able to read data that you write after this point
    f.write('this is test text\n')
    f.seek(0)  # Important: return to the top of the file before reading, otherwise you'll just read an empty string
    data = f.read() # Returns 'somedata\n'
    print(data)







