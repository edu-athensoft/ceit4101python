"""
Container
Toplevel
"""

from tkinter import *
import random


def message():
    msg = {1: "Yes", 2: "No", 3: "Exit"}
    msgType = random.randint(1, 3)

    topframe = Toplevel()
    topframe.geometry("300x180+320+280")
    topframe.title("Message Box")

    labTxt = msg[msgType]
    Label(topframe, text=labTxt, bg="lightgreen").pack(fill=BOTH, expand=True)


# main program
root = Tk()
root.title("Python GUI - Toplevel")
root.geometry("640x480+300+200")
root.config(bg="#ddddff")

btn = Button(root, text="Show toplevel frame", command=message)
btn.pack()

root.mainloop()
