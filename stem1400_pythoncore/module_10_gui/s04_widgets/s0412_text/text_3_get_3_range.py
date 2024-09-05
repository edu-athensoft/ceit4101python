"""
Text widget

get text content of specified range
"""

from tkinter import *


def get_text():
    START_POS = "1.5"
    END_POS = "2.3"
    content = text.get(START_POS, END_POS)
    print(content)


root = Tk()
root.title("Python GUI | Text")

# text widget
text = Text(root, height=5, width=30)
text.pack(fill=BOTH, expand=Y)

# inserting text content
text.insert(END, "INITIxx xxxxx x\n")
text.insert(END, "xxxTIAL VALUE b\n")
text.insert(END, "INITIAL VALUE c")

# press to get
btn = Button(root, text="Get text in range", command=get_text)
btn.pack()

root.mainloop()
