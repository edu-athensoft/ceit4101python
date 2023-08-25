"""
Scale

basic usage of Scale

get value via Scale object
"""

from tkinter import *


def printValue():
    print("print value 1",scale1.get())


def printValue2():
    print("print value 2",scale2.get())


# main program
root = Tk()
root.title("Python GUI - Scale")
root.geometry("640x480")

# label
label = Label(root, text="A simple demo of Scale", bg="lightyellow", width=30)
label.pack()

var1 = IntVar()
scale1 = Scale(root, from_=0, to=10)
scale1.pack()

Button(root, text="Print value of Scale #1", width=20, command=printValue).pack()


var2 = IntVar()
scale2 = Scale(root, from_=0, to=10, orient=HORIZONTAL)
scale2.pack()

Button(root, text="Print value of Scale #2", width=20, command=printValue2).pack()

root.mainloop()
