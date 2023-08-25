"""
Protocol

Redefine exit
"""

from tkinter import *
from tkinter import messagebox


def callback():
    res = messagebox.askokcancel("Exit", "Are you sure to exit?")
    # True or False
    if res:
        root.destroy()
    else:
        return


root = Tk()
root.title("Event Handling | Protocols")
root.geometry("320x120")
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()
