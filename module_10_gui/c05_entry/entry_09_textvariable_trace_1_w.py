"""
textvariable

trace()
"""

from tkinter import *


def callbackW(*args):
    print("data changed:", xE.get())


root = Tk()
root.title("Python GUI - Entry")
root.geometry("360x160")

xE = StringVar()

entry = Entry(root, textvariable = xE)
entry.pack()

xE.trace('w', callbackW)

root.mainloop()

