"""
text
adding X-scrollbar
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text X-Scrollbar")
root.geometry("320x180+300+200")

# text
text = Text(root, height=5, width=30, wrap=NONE)
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# scrollbar
scrollbar = Scrollbar(root, command=text.xview, orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)

# link scrollbar to text widget
text.config(xscrollcommand=scrollbar.set)

# layout
text.pack(side=LEFT, fill=BOTH, expand=YES)

root.mainloop()