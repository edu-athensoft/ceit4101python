"""
fileno()
"""

import os

with open("example.txt", "r") as file:
    fd = file.fileno()

    # Get file stats using the descriptor
    stats = os.fstat(fd)
    print(f"File size: {stats.st_size} bytes")
