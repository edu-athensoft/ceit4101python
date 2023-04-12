"""
text
"""

from tkinter import *
from tkinter.ttk import Separator


def countlines(event):
    (line, c) = map(int, event.widget.index("end-1c").split("."))
    # print(line, c)
    status_text1 = f"Status: INSERT MODE  ROW:{line},COL:{c}"
    var.set(status_text1)


def func1():
    str_status = var.get()
    status_text2 = ' '*5+"Func1 was called."
    var.set(status_text1+status_text2)
    status_text2 = ''


def func2():
    str_status = var.get()
    status_text2 = ' '*5+"Func2 was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''


def func3():
    str_status = var.get()
    status_text2 = ' '*5+"Func3 was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''


root = Tk()
root.title("Athensoft Python Course | Text")
root.geometry("640x480+300+300")

# toolbar frame
frame_toolbar = Frame(root, height=30)
frame_toolbar.pack(anchor=W)

btn1 = Button(frame_toolbar, text='Func1', command=func1)
btn1.pack(side=LEFT)

btn2 = Button(frame_toolbar, text='Func2', command=func2)
btn2.pack(side=LEFT)

btn3 = Button(frame_toolbar, text='Func3', command=func3)
btn3.pack(side=LEFT)

# text widget
text = Text(root, height=5, width=30)
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

# for mode and position
status_text1= "Status: INSERT MODE"

statusbar = Label(root, textvariable=var)
statusbar.pack(anchor=S + W)
var.set(status_text1)

# for function button clicked
status_text2 = ""

root.mainloop()
