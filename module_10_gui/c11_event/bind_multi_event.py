"""
Binding multiple events
"""

from tkinter import *


def click1():
    print("1. Command event handler")


def click2(event):
    print("2. Bind event handler")


root = Tk()
root.title("Event Handling | Unbind")
# root.geometry("640x480")

btn = Button(root, text="Multiple Events", command=click1)
btn.pack(anchor=CENTER, padx=120, pady=50)

btn.bind("<Button-1>", click2, add="+")

root.mainloop()
