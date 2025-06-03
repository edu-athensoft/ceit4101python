"""
fileno()


When a file descriptor equals 3, it means that the operating system has assigned the
integer 3 to an open file or file-like resource for identifying and managing it.

Context:
File descriptors are integers used by the operating system to keep track of open files,
sockets, or other I/O resources.
The first three file descriptors are generally reserved for standard streams:
0: Standard Input (stdin)
1: Standard Output (stdout)
2: Standard Error (stderr)
Any file or resource opened beyond these standard descriptors is typically
assigned the next available file descriptor. So, 3 would usually represent
the first file or resource opened after the standard streams.
"""

# Open a file
with open("example.txt", "r") as file:
    # Get the file descriptor
    fd = file.fileno()
    print(f"File descriptor for 'example.txt': {fd}")
