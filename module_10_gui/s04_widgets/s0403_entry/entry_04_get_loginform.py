"""
Entry
padx(left, right)

get()

"""

from tkinter import *
from tkinter.ttk import Separator


def printInfo():
    print(f"Account:{accountE.get()}\nPassword:{passwordE.get()}")


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

loginbtn = Button(root, text = "Login", command = printInfo)
loginbtn.grid(row=4, column = 0, sticky="e")

quitbtn = Button(root, text = "Quit", command = root.destroy)
quitbtn.grid(row=4, column = 1, sticky="w")

sep = Separator(root)
sep.grid(row=5, columnspan=2, sticky="nswe", padx=2, pady=5)

labelFooter = Label(root, text="Copyright 2021 Athensoft Inc. ")
labelFooter.grid(row=6, columnspan=2)

root.mainloop()
