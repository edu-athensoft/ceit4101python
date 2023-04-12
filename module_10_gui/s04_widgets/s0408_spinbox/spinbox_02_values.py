"""
Spinbox

a value sequence is allowed
including both numeric and non-numeric values

"""

from tkinter import *


def getNum(widget):
    print(widget.get())


root = Tk()
root.title("Python GUI - Spinbox")
root.geometry("360x240")

spin = Spinbox(root, values=(10, 21, 32, 43), font=(None, 15))
spin.config(command=lambda: getNum(spin))
spin.pack()

spin2 = Spinbox(root, values=('Python', 'Java', 'Web', 'Database', 'OS'), font=(None, 15))
spin2.config(command=lambda: getNum(spin2))
spin2.pack()

root.mainloop()
