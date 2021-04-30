"""
place()

https://www.geeksforgeeks.org/python-place-method-in-tkinter/
"""

# Importing tkinter module
from tkinter import *
from tkinter.ttk import *

# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("200x200")
root.config(bg='#ddddff')

# button widget
b1 = Button(root, text="Click me")
# b1.place(relx=1, x=-2, y=2, anchor=NE)
b1.place(relx=0.2, x=-2, y=2)  # does not show

# label widget
lab = Label(root, text="I'm a Label")
lab.place(anchor=NW)

# button widget
b2 = Button(root, text="Button")
b2.place(relx=0.5, rely=0.5, anchor=CENTER)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()