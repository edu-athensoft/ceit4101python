"""
Tkinter

create a button
pack layout

and set state for a button

ref: #3
"""


from tkinter import *


root = Tk()

btn1 = Button(root, text='Confirm')
btn1.pack()

# the state must be active, disabled, or normal
btn2 = Button(root, text='Confirm', state='active')
btn2.pack()

btn3 = Button(root, text='Confirm', state='disabled')
btn3.pack()

btn4 = Button(root, text='Confirm', state='normal')
btn4.pack()

root.mainloop()