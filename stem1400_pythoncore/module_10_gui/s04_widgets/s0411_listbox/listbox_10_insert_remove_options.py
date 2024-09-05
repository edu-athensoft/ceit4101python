"""
Listbox
Event binding - ListboxSelect
"""

from tkinter import *


def itemAdded():
    varAdd = entry.get()
    if len(varAdd.strip()) == 0:
        return
    lb.insert(END, varAdd)
    entry.delete(0, END)


def itemDeleted():
    index = lb.curselection()
    if len(index) == 0:
        return
    lb.delete(index)


root = Tk()
root.title("Python GUI - Listbox")
root.config(bg="#ddddff")

entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)

btnAdd = Button(root, text="Add option", width=10, command=itemAdded)
btnAdd.grid(row=0, column=1, padx=5, pady=5)

lb = Listbox(root)
lb.grid(row=1, column=0, columnspan=2, padx=5, pady=5, stick=W)

btnDel = Button(root, text="Remove option", width=15, command=itemDeleted)
btnDel.grid(row=2, column=0, padx=5, pady=5, stick=W)

root.mainloop()
