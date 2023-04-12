"""
Listbox
create a simple listbox
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

# create a listbox
mylistbox = Listbox(root)
mylistbox.pack(pady=30)

root.mainloop()