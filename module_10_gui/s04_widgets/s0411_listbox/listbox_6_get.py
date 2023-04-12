"""
Listbox
get(index)
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("340x280+300+200")
root.config(bg="#ddddff")

# create a listbox
mylistbox = Listbox(root)
mylistbox.pack(pady=30)

# insert options
items = ["Item 0", "Item 1", "Item 2"]

for item in items:
    mylistbox.insert(END, item)

myoption = mylistbox.get(0)
print(myoption, type(myoption))

root.mainloop()