"""
text
ScrolledText with default scrollbar
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Python GUI | ScrolledText")
root.geometry("320x180+300+200")

# ScrolledText
text = ScrolledText(root, height=5, width=30, undo=True)
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# layout
text.pack(side=LEFT, fill=BOTH, expand=YES)

root.mainloop()
