"""
Text widget

get text content of current line
"""

from tkinter import *


def get_text():
    line_num = text.index(INSERT).split(".")[0]
    content = text.get(f"{line_num}.0", f"{line_num}.end")
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
btn = Button(root, text="Get current line", command=get_text)
btn.pack()

root.mainloop()
