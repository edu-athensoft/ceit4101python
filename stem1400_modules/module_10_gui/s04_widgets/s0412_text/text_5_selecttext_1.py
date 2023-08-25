"""
text
select text
"""

from tkinter import *


def selectedText():
    try:
        selText = text.get(SEL_FIRST, SEL_LAST)
        print("Selected text:")
        print(selText)
    except TclError:
        print("No text selected.")


root = Tk()
root.title("Python GUI | Text Selecting")
root.geometry("640x480+300+200")

# text
text = Text(root, height=5, width=30)
text.insert(END, "aaaabbbbcccc1111\n")
text.insert(END, "aaaabbbbcccc2222\n")
text.insert(END, "aaaabbbbcccc3333")

# frame
frame_toolbar = Frame(root)

# btn
btn = Button(frame_toolbar, text="Print selection", command=selectedText)

# layout
frame_toolbar.pack(anchor=W)
btn.pack(side=LEFT)
text.pack(fill=BOTH, expand=Y)

root.mainloop()
