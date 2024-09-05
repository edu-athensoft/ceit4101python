"""
text
"""

from tkinter import *
from tkinter.ttk import Separator


def countlines(event):
    (line, c) = map(int, event.widget.index("end-1c").split("."))
    # print(line, c)

    var.set(f"Status: INSERT MODE  ROW:{line},COL:{c}")

root = Tk()
root.title("Athensoft Python Course | Text")
root.geometry("640x480+300+300")

# text widget
text = Text(root, height = 5, width = 30)
text.pack(fill=BOTH, expand=Y)

# init text
# text.insert(END, "Python\nTkinter\n")
# text.insert(END, "I like you.")

text.bind("<KeyRelease>", countlines)


# separator
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# status bar
var = StringVar()
var.set("Status: INSERT MODE")
statusbar = Label(root, textvariable=var)
statusbar.pack(anchor=S+W)

root.mainloop()