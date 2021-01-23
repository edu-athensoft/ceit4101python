"""
Tkinter

place a label widget

using pack() layout

ref: #1
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label dimension')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Tkinter Label Dimension', height=3, width=40)
# show on screen
label1.pack()

# create a label widget
label2 = Label(root, text='Tkinter Label Dimension', height=7, width=20)
# show on screen
label2.pack()

root.mainloop()