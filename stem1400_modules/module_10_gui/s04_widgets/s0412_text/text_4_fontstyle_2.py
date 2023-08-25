"""
text
font style
font family
"""

from tkinter import *
from tkinter.font import Font


def change_fontfamily():
    TEXT_FONT.config(family="Arial")
    text.configure(font=TEXT_FONT)


def change_fontfamily_2():
    TEXT_FONT.config(family="Times New Roman")
    text.configure(font=TEXT_FONT)


def change_fontfamily_3():
    TEXT_FONT.config(family="Consolas")
    text.configure(font=TEXT_FONT)


def change_fontsize(num):
    # f = Font(size=num)
    # f = TEXT_FONT
    TEXT_FONT.config(size=num)
    text.configure(font=TEXT_FONT)


root = Tk()
root.title("Python GUI | Text Font Style")
root.geometry("640x480+300+200")

# settings
TEXT_FONT = Font(family="Arial", weight="normal", size=10)

# text
text = Text(root, height=5, width=30)
text.insert(END, "Font Style\n")
text.insert(END, "font family\n")
text.insert(END, "font weight\n")
text.insert(END, "font size")

# frame
frame_toolbar = Frame(root)

# btn
btn1_family = Button(frame_toolbar, text="Arial", command=change_fontfamily)
btn2_family = Button(frame_toolbar, text="Times new roman", command=change_fontfamily_2)
btn3_family = Button(frame_toolbar, text="Consolas", command=change_fontfamily_3)

btn1_size = Button(frame_toolbar, text="10pt", command=lambda: change_fontsize(10))
btn2_size = Button(frame_toolbar, text="12pt", command=lambda: change_fontsize(12))
btn3_size = Button(frame_toolbar, text="16pt", command=lambda: change_fontsize(16))

# layout
frame_toolbar.pack(anchor=W)
btn1_family.pack(side=LEFT)
btn2_family.pack(side=LEFT)
btn3_family.pack(side=LEFT)
btn1_size.pack(side=LEFT)
btn2_size.pack(side=LEFT)
btn3_size.pack(side=LEFT)

text.pack(fill=BOTH, expand=Y)

root.mainloop()
