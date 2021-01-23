"""
Tkinter

overlapping

using grid layout

relative position

ref: #2
"""


from tkinter import *


root = Tk()
root.geometry('640x480+50+50')

# create a label widget
label1 = Label(root, text='Athensoft').grid(row=0, column=0)
label2 = Label(root, text='Python Programming').grid(row=2, column=3)
label3 = Label(root, text='III').grid(row=3, column=5)

# show on screen
# observe the result by the same row and column
# part of the results are overlapping

root.mainloop()