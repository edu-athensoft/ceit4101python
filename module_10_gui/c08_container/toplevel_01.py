"""
Container
Toplevel
"""

from tkinter import *
import random


def MessageBox():
    msgType = random.randint(1, 3)
    labTxt = msg[msgType]
    topframe = Toplevel()
    topframe.geometry("300x180")
    topframe.title("Message Box")
    Label(topframe, text=labTxt, bg="lightgreen").pack(fill=BOTH, expand=True)


# main program
root = Tk()
root.title("Python GUI - Toplevel")
root.geometry("320x160")
root.config(bg="#ddddff")

msg = {1: "Yes", 2: "No", 3: "Exit"}

btn = Button(root, text="Show toplevel frame", command=MessageBox)
btn.pack()

root.mainloop()
