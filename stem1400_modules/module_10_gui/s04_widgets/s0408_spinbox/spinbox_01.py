"""
Spinbox

increment - a step number which can be set by programmer

"""

from tkinter import *


def getNum():
    print(spin.get())


root = Tk()
root.title("Python GUI - Spinbox")
root.geometry("360x240")

spin = Spinbox(root, from_=1, to=10, increment=1, command=getNum,
               font=(None,15))
spin.pack()

root.mainloop()
