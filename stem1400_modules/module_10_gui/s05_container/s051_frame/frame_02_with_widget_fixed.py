"""
frame
"""
from tkinter import *
win = Tk()
frame1 = Frame(win, width=400, height=200, bg="lightgreen")
frame1.pack(fill=X)
frame2 = Frame(win, width=400, height=200, bg="lightyellow")
frame2.pack(fill=X)

frame1.pack_propagate(False)
frame2.pack_propagate(False)

label1 = Label(frame1, text="Label 1 in Frame 1")
label2 = Label(frame2, text="Label 2 in Frame 2")

label1.pack()
label2.pack()

win.mainloop()