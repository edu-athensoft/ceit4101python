"""
module:     GUI and tkinter
topic:      place layout
section:    5.3.2 relx / rely
problem:    n/a
ver:        1
file:       place_03_relxrely.py
"""

from tkinter import *

root = Tk()
root.title('Python GUI - place')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

p1 = Label(root, text='Label 1')
p2 = Label(root, text='Label 2')

p1.place(x=50, y=50)

# p2 does not show
p2.place(relx=0.3, rely=0.3)

# does not show
# p2.place(relx=2, rely=2)

root.mainloop()
