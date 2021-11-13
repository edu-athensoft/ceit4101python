"""
menu

basic menu and menu option
"""

from tkinter import *
from tkinter import messagebox


def test_menu1():
    messagebox.showinfo("Test", "Menu 1 is clicked")


def test_menu2():
    messagebox.showinfo("Test", "Menu 2 is clicked")


root = Tk()
root.title("Athensoft Python Course | Menu")
root.geometry("640x480+300+300")

# define menu and menu items
menubar = Menu(root)
menubar.add_command(label="MENU_1", command=test_menu1)
menubar.add_command(label="MENU_2", command=test_menu2)
menubar.add_command(label="Exit", command=root.destroy)

# set menu
root.config(menu=menubar)

root.mainloop()
