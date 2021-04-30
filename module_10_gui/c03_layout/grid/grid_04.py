"""
Tkinter

using grid layout

relative position

ref: #2
"""


from tkinter import *


root = Tk()
root.geometry('640x480+200+200')
root.config(bg='#ddddff')

# create label widgets
label1 = Label(root, text='Label 1',bg='yellow')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')
label4 = Label(root, text='Label 4',bg='yellow')

# show on screen
label1.grid(row=0, column=0, rowspan=2)
label2.grid(row=0, column=1)
label3.grid(row=1, column=1)

root.mainloop()