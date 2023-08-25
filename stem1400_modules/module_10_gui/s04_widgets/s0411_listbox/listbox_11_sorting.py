"""
Listbox
Sorting items
"""

from tkinter import *


def itemSorted():
    listTmp = list(lb.get(0, END))
    sortedList = sorted(listTmp, reverse=var.get())
    lb.delete(0, END)
    for item in sortedList:
        lb.insert(END, item)


root = Tk()
root.title("Python GUI | Listbox")

fruits = ["Banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]

lb = Listbox(root)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(padx=10, pady=5)

btn = Button(root, text="Ascending Sort", command=itemSorted)
btn.pack(side=LEFT, padx=10, pady=5)

var = BooleanVar()
cb = Checkbutton(root, text="Descending Sort", variable=var)
cb.pack(side=LEFT)

root.mainloop()
