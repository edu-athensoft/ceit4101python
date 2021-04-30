"""
Tkinter

place a label widget
Label(parent_object, options,...)

using pack() layout

ref: #1
"""


from tkinter import *

root = Tk()
root.title('Python GUI - Text Label')
root.geometry("{}x{}+200+240".format(640, 480))

# create a label widget
label1 = Label(root, text='Tkinter Label 1')

# show on screen
label1.pack()


# create a label widget
label2 = Label(root, text='Tkinter Label 2')

# show on screen
label2.pack()

root.mainloop()
