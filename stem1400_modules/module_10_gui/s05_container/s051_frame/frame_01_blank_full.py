"""
frame
"""
from tkinter import *

root = Tk()
root.title("Frame")
root.config(bg="#ddddff")
root.geometry("640x400")

frame1 = Frame(root, width=400, height=200, bg="lightgreen")
frame1.pack(fill=X)

frame2 = Frame(root, width=400, height=200, bg="lightyellow")
frame2.pack(fill=X)

root.mainloop()