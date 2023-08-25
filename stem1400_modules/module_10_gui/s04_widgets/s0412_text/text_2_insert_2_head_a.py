"""
Text widget

insert at head
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert("1.0", "INITIAL TEXT")

root.mainloop()
