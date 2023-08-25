"""
Text widget

create
"""

from tkinter import *


root = Tk()
root.title("Python GUI | Text")
root.geometry("420x120+300+300")

text = Text(root, height = 5, width = 30)
text.pack()

root.mainloop()