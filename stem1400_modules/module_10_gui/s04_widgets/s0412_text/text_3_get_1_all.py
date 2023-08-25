"""
Text widget

get all text content
"""

from tkinter import *


def get_text():
    content = text.get("1.0", END)
    print(content)


root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert(END, "INITIAL VALUE a\n")
text.insert(END, "INITIAL VALUE b\n")
text.insert(END, "INITIAL VALUE c")

# press to get
btn = Button(root, text="Get all text", command=get_text)
btn.pack()

root.mainloop()
