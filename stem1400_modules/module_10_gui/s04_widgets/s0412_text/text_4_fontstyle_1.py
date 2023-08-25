"""
text
font style
font family
"""

from tkinter import *
from tkinter.font import Font


def change_fontfamily():
    f = Font(family="Arial", weight="bold")
    text.configure(font=f)


def change_fontfamily_2():
    f = Font(family="Times New Roman", weight="normal")
    text.configure(font=f)


def change_fontfamily_3():
    f = Font(family="Consolas", weight="normal")
    text.configure(font=f)


root = Tk()
root.title("Python GUI | Text Font Style")
root.geometry("640x480+300+200")

# text
text = Text(root, height=5, width=30)
text.insert(END, "Font Style\n")
text.insert(END, "font family\n")
text.insert(END, "font weight\n")
text.insert(END, "font size")

# frame
frame_toolbar = Frame(root)

# btn
btn = Button(frame_toolbar, text="Arial", command=change_fontfamily)
btn2 = Button(frame_toolbar, text="Times new roman", command=change_fontfamily_2)
btn3 = Button(frame_toolbar, text="Consolas", command=change_fontfamily_3)

# layout
frame_toolbar.pack(anchor=W)
btn.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
text.pack(fill=BOTH, expand=Y)

root.mainloop()
