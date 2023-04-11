"""
Layout manager:  pack()

side
homework: list relief from left to right

"""


from tkinter import *
from tkinter.ttk import Separator

root = Tk()

# root.geometry('640x480+0+0')
root.config(bg='#ddddff')

reliefs = ["flat", "groove", "raised","ridge", "solid", "sunken"]
for myrelief in reliefs:
    Label(root,
          text=myrelief, relief=myrelief,
          fg="blue", font="Arial 20 bold").pack(side=LEFT, padx=5, ipadx=10)

# sep = Separator(root, orient= HORIZONTAL)
# sep.pack(side= LEFT, fill = Y, padx=5)
#
# for myrelief in reliefs:
#     Label(root,
#           text=myrelief, relief=myrelief,
#           fg="red", font="Arial 20 bold").pack(side=LEFT, padx=10, ipadx=5)

root.mainloop()

