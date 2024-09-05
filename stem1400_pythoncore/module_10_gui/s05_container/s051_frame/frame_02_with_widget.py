"""
Container
Frame
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Frame")
root.geometry("300x200")
# root.config(bg="#ddddff")
# print(root.keys())

frameUpper = Frame(root, bg="lightgreen", height=150, width=200)
frameUpper.pack()

btnRed = Button(frameUpper, text="Red", fg="red").pack(side=LEFT)
btnGreen = Button(frameUpper, text="Green", fg="green").pack(side=LEFT)

frameLower = Frame(root, bg="lightyellow", height=150, width=200)
# frameLower.pack(fill=BOTH, expand=True)
frameLower.pack()

btnPurple = Button(frameLower, text="Purple", fg="purple")
btnPurple.pack(side=BOTTOM)
root.mainloop()
