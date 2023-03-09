"""
module:     GUI and tkinter
topic:      place layout
section:    5.3.1 x / y
problem:    n/a
ver:        1
file:       place_01_xy.py
"""

from tkinter import *

root = Tk()
root.title('Python GUI - place')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

p1 = Label(root, text='Label 1')
p2 = Label(root, text='Label 2')

p1.place(x=100, y=100)
p2.place(x=200, y=31)

root.mainloop()
