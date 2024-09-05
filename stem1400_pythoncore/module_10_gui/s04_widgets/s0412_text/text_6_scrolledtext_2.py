"""
text
ScrolledText with x-scrollbar and y-scrollbar
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Python GUI | ScrolledText")
root.geometry("320x180+300+200")

# tk version
print(TkVersion)

# scrolled text
text = ScrolledText(root, height=5, width=30, wrap='none')
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# scrollbar
xscrollbar = Scrollbar(root, orient=HORIZONTAL, command=text.xview)
text.configure(xscrollcommand=xscrollbar.set)

# layout
xscrollbar.pack(fill=X, side=BOTTOM)
text.pack(side=LEFT, fill=BOTH, expand=YES)

# print(dir(ScrolledText))

root.mainloop()
