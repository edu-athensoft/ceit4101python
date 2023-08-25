"""
Level 2 menu item (option)
"""

from tkinter import *
from tkinter import messagebox


def newfile():
    messagebox.showinfo("File", "New File")


def openfile():
    messagebox.showinfo("File", "New File")


def save():
    messagebox.showinfo("File", "New File")


def saveas():
    messagebox.showinfo("File", "New File")


root = Tk()
root.title("Athensoft Python Course | Menu")
root.geometry("640x480+300+300")

# main menu
menubar = Menu(root)

# main menu item
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)

# level 2 menu options
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open File", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=saveas)
# filemenu.add_command(label="Exit", command=root.destroy)

# set menu to window
root.config(menu=menubar)

root.mainloop()
