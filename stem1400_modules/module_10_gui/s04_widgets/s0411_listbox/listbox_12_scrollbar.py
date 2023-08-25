"""
link scrollbar to listbox
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("340x280+300+200")
root.config(bg="#ddddff")

# frame for listbox and scrollbar
frame1 = Frame(root)
frame1.pack()

# listbox
listbox1 = Listbox(frame1, height=8)
listbox1.insert(END, "item 1")
listbox1.insert(END, "item 2")
listbox1.insert(END, "item 3")
listbox1.insert(END, "item 4")
listbox1.insert(END, "item 5")
listbox1.insert(END, "item 6")
listbox1.insert(END, "item 7")
listbox1.insert(END, "item 8")
listbox1.insert(END, "item 9")
listbox1.insert(END, "item 10")

# scrollbar
yscrollbar = Scrollbar(frame1)

# link
yscrollbar.config(command=listbox1.yview)
listbox1.config(yscrollcommand=yscrollbar.set)

# layout
listbox1.pack(side=LEFT, fill=BOTH)
yscrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()
