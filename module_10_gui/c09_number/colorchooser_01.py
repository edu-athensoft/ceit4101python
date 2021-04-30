"""
Color chooser

"""

from tkinter import *
from tkinter.colorchooser import *


def changeColor():
    """change background color of window"""
    myColor = askcolor()
    print(myColor, type(myColor))
    root.config(bg=myColor[1])


root = Tk()
root.title("Python GUI - Color Chooser")
root.geometry("360x240")

btn = Button(text="Color chooser", command=changeColor).pack()

root.mainloop()
