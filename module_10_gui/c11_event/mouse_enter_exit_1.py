"""
Event handling
Mouse event
<Motion>
"""

from tkinter import *


def handler_enter(event):
    position_str = 'Mouse entered'
    print(position_str)
    var.set(position_str)

def handler_exit(event):
    position_str = 'Mouse left'
    print(position_str)
    var.set(position_str)

# main program
root = Tk()
root.title("Python GUI - Event | Mouse")
root.geometry("640x480+300+300")

# label
var = StringVar()
var.set('Move your mouse to enter and leave the Label')
label1 = Label(root, textvariable=var, font=("Helvetica",16),
               width=35, height=16, relief='groove',bg="#ddddff")
label1.pack(padx=20, pady=40, anchor=CENTER)

# mouse event: Enter - move in
root.bind("<Enter>", handler_enter)

# mouse event: Leave - move out
root.bind("<Leave>", handler_exit)

root.mainloop()
