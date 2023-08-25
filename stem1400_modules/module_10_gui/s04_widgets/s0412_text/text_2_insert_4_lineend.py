"""
Text widget

insert at line end
"""

from tkinter import *


def insert_text():
    insert_pos = text.index(INSERT)
    line_num = int(insert_pos.split('.')[0])
    text.insert(f"{line_num}.end", "aaa")


root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert(END, "INITIAL TEXT LINE 1\n")
text.insert(END, "INITIAL TEXT LINE 2\n")
text.insert(END, "INITIAL TEXT LINE 3\n")

# press to insert
btn = Button(root, text="Insert at line end", command=insert_text)
btn.pack()

root.mainloop()
