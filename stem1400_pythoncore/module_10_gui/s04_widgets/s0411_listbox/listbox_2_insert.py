"""
Listbox
insert options at tail
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("640x280+300+200")
root.config(bg="#ddddff")

# create a listbox
mylistbox = Listbox(root)
mylistbox.pack(pady=30)

# insert options
items = ["Item 1", "Item 2", "Item 3"]

for item in items:
    mylistbox.insert(END, item)

root.mainloop()