"""
text
adding Y-scrollbar and X-scrollbar
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text Scrollbar")
root.geometry("320x180+300+200")

# text
text = Text(root, height=5, width=30, wrap=NONE)
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# y-scrollbar
yscrollbar = Scrollbar(root, command=text.yview)
yscrollbar.pack(side=RIGHT, fill=Y)

# x-scrollbar
xscrollbar = Scrollbar(root, command=text.xview, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

# link scrollbar to text widget
text.config(yscrollcommand=yscrollbar.set)
text.config(xscrollcommand=xscrollbar.set)

# layout
text.pack(side=LEFT, fill=BOTH, expand=YES)

root.mainloop()