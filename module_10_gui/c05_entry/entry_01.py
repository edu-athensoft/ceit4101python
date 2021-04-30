"""
Entry
padx(left, right)

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")

accountL = Label(root, text="Account ")
accountL.grid(row=2,padx=(50,5), sticky='e')

passwordL = Label(root, text="Password ")
passwordL.grid(row=3,padx=(50,5), sticky='e')

accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))

passwordE = Entry(root, show='*')
passwordE.grid(row=3, column=1, padx=(5, 50))

root.mainloop()
