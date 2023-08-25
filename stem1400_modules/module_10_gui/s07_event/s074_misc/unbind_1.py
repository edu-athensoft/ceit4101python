"""
Unbinding event
"""

from tkinter import *


def click_btn(event):
    print("This button was clicked.")


def toggle(widget):
    if var.get():
        widget.bind("<Button-1>", click_btn)
    else:
        widget.unbind("<Button-1>")


root = Tk()
root.title("Event Handling | Unbind")
root.geometry("640x480")

btn = Button(root, text="Click me!")
btn.pack(anchor=W, padx=10, pady=10)

var = BooleanVar()
chkbtn = Checkbutton(root, text="Bind/Unbind", variable=var, command=lambda : toggle(btn))
chkbtn.pack(anchor=W, padx=10)

root.mainloop()
