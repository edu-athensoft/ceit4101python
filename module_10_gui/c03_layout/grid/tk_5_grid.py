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
label3 = Label(root, text='III')

# show on screen
# relative position
label1.grid(row=0, column=0)
label2.grid(row=1, column=5)
label3.grid(row=2, column=1)

root.mainloop()