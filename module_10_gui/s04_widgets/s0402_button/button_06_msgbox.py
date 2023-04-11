#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Tkinter
Button &  MessageBox
click and response
lambda
"""


from tkinter import *
from tkinter import messagebox as msg


def helloCallBack():
   title = "Show Messegebox"
   text = "Hello Python Tkinter"
   msg.showinfo(title, text)


root = Tk()
root.title('Python GUI - Button and Messagebox')
root.geometry('300x200')

# option 1. lambda
btn1 = Button(root, text='Show Messagebox', command=lambda:helloCallBack())

# option 2. function name
btn2 = Button(root, text='Close', command=root.destroy)


btn1.grid(sticky=S, row=1, column=0, pady=(160,0), padx=(80,0))
btn2.grid(sticky=S, row=1, column=1)

root.mainloop()
