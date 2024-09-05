"""
text
adding Y-scrollbar
"""

from tkinter import *

root = Tk()
root.title("Python GUI | Text Y-Scrollbar")
root.geometry("320x180+300+200")

# text
text = Text(root, height=5, width=30)
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# scrollbar
scrollbar = Scrollbar(root, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# link scrollbar to text widget
text.config(yscrollcommand=scrollbar.set)

# layout
text.pack(side=LEFT, fill=BOTH, expand=YES)

root.mainloop()