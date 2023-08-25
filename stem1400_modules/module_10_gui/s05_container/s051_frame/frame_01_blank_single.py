"""
Frame - a container widget

create a frame in main window
"""
from tkinter import *

root = Tk()
root.title("Frame")
root.config(bg="#ddddff")
root.geometry("640x320")

frame1 = Frame(root, width=600, height=200, bg="lightgreen")
frame1.pack()

root.mainloop()