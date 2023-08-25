"""
Text widget

insert at END
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert(END, "INITIAL TEXT")

root.mainloop()
