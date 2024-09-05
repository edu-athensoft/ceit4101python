"""
Text widget

insert at INSERT
"""

from tkinter import *


def insert_text():
    pos = f"{text.index(INSERT)}+3c"
    text.insert(pos, "aaa")


root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert(END, "INITIAL TEXT")

# press to insert
btn = Button(root, text="Insert at INSERT", command=insert_text)
btn.pack()

root.mainloop()
