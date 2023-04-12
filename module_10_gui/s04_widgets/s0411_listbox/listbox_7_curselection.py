"""
Listbox
get(index)
"""

from tkinter import *


def callback():
    indexes = mylistbox.curselection()
    for index in indexes:
        print(index, mylistbox.get(index))


langs = ["Python", "Java", "C++", "Go", "Javascript", "C#"]

root = Tk()
root.title("Python GUI - Listbox")
root.geometry("340x320+300+200")
root.config(bg="#ddddff")

mylistbox = Listbox(root, selectmode=EXTENDED)
for lang in langs:
    mylistbox.insert(END, lang)
mylistbox.pack(pady=30)

btn = Button(root, text="Print", command=callback)
btn.pack(pady=5)

root.mainloop()
