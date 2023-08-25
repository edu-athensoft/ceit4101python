"""
Text widget

create
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)
# text.pack()

root.mainloop()
