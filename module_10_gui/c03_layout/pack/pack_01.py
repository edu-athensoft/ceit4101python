"""
Layout manager:  pack()

-after, -anchor, -before, -expand, -fill,
-in, -ipadx, -ipady, -padx, -pady, -side
"""


from tkinter import *


root = Tk()

label1 = Label(root, text='Python')
label2 = Label(root, text='Java')
label3 = Label(root, text='Web')
label4 = Label(root, text='Database')

root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1.pack()
label2.pack()
label3.pack()
label4.pack()

root.mainloop()

