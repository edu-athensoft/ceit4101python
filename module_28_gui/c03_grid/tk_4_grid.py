"""
Tkinter

using grid layout

relative position

ref: #2
"""


from tkinter import *


root = Tk()

# create a label widget
label1 = Label(root, text='Athensoft')
label2 = Label(root, text='Python Programming')

# show on screen
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

# relative position
# label2.grid(row=1, column=5)

root.mainloop()