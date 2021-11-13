"""
multi menu items
multi level 2 menu options
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


def copy():
    messagebox.showinfo("Edit", "copy")


def cut():
    messagebox.showinfo("Edit", "cut")


def paste():
    messagebox.showinfo("Edit", "paste")


root = Tk()
root.title("Athensoft Python Course | Menu")
root.geometry("640x480+300+300")

# main menu
menubar = Menu(root)

# main menu item - file
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# level 2 menu options
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open File", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=saveas)
# filemenu.add_command(label="Exit", command=root.destroy)


# main menu item - edit
editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=editmenu)
# level 2 menu options
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Paste", command=paste)

# set menu to window
root.config(menu=menubar)

root.mainloop()
