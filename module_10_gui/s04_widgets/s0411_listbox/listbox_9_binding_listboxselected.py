"""
Listbox
Event binding - ListboxSelect
"""

from tkinter import *


def itemSelected(event):
    obj = event.widget
    index = obj.curselection()
    var.set(obj.get(index))


fruits = ["Banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("340x320+300+200")
root.config(bg="#ddddff")

var = StringVar()
lab = Label(root, text="", textvariable=var)
lab.pack(pady=5)

lb = Listbox(root, selectmode=SINGLE)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(pady=10)
lb.bind("<<ListboxSelect>>", itemSelected)

root.mainloop()
