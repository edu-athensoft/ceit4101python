"""
Tkinter

place a label widget

using pack() layout

ref: #1
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label color')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Label color',
               height=3, width=40,
               bg='#EF72AA', fg='white')
# show on screen
label1.pack()

# create a label widget
label2 = Label(root, text='Label Dimension',
               height=7, width=20,
               bg='#72EFAA', fg='black')
# show on screen
label2.pack()

root.mainloop()