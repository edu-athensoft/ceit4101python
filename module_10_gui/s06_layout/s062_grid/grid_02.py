"""
Tkinter

using grid layout

ref: #2
"""


from tkinter import *


root = Tk()
root.geometry('640x480+200+200')
root.config(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')
label4 = Label(root, text='Label 4')
label5 = Label(root, text='Label 5')

# show on screen
label1.grid()
label2.grid(column=1)
label3.grid(column=2)
label4.grid(column=3)
label5.grid(column=5)

root.mainloop()
