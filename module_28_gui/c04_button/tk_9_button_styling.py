"""
Tkinter

create a button
pack layout

styling button

size: padx, pady

color: fg and bg

ref: #3
"""


from tkinter import *


root = Tk()

btn1 = Button(root, text='Confirm')
btn1.pack()

btn2 = Button(root, text='Click', padx=50, pady=10)
btn2.pack()

btn3 = Button(root, text='Click', padx=50, pady=10, fg="white",bg="blue")
btn3.pack()

btn3 = Button(root, text='Click', padx=50, pady=10, fg="white",bg="#ff0000")
btn3.pack()

root.mainloop()