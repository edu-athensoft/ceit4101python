"""
popup menu

"""

from tkinter import *
from tkinter import messagebox


def copy():
    print("copy")


def cut():
    print("cut")


def paste():
    print("paste")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


root = Tk()
root.title("Athensoft Python Course | Popup Menu")
root.geometry("640x480+300+300")

# popup menu
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Copy", command=copy)
popupmenu.add_command(label="Cut", command=cut)
popupmenu.add_separator()
popupmenu.add_command(label="Paste", command=paste)

# binding to root
root.bind("<Button-3>", showPopupMenu)


root.mainloop()
