"""
layout with grid

form
"""


from tkinter import *

master = Tk()
master.geometry('640x480+50+50')
Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=2)


e1 = Entry(master)
e2 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=2, column=1)

mainloop()