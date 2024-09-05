"""
Entry
padx(left, right)

"""

from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")

labelTitle = Label(root, text="Login Form", font=("Segoe UI", 16, "bold", "roman"))
labelTitle.grid(row=0, columnspan=2)

sep = Separator(root)
sep.grid(row=1, columnspan=2, sticky="nswe", padx=2, pady=5)


accountL = Label(root, text="Account ")
accountL.grid(row=2,padx=(50,5), sticky='e')

passwordL = Label(root, text="Password ")
passwordL.grid(row=3,padx=(50,5), sticky='e')

accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))

passwordE = Entry(root, show='*')
passwordE.grid(row=3, column=1, padx=(5, 50))

loginBtn = Button(root, text="Login")
loginBtn.grid(row=4, column=0, columnspan=2, pady=3)

sep = Separator(root)
sep.grid(row=5, columnspan=2, sticky="nswe", padx=2, pady=5)

labelFooter = Label(root, text="Copyright 2021 Athensoft Inc. ")
labelFooter.grid(row=6, columnspan=2)

root.mainloop()
