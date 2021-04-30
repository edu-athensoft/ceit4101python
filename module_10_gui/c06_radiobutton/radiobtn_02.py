"""
Radiobutton

using dictionary

"""

from tkinter import *


def printOption():
    print(roles[var.get()])


# main program
root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("320x120")

roles = {0:'Mage', 1: 'Warrior', 2: 'Archer'}
var = IntVar()
var.set(0)

label = Label(root, text="Your role", bg="lightyellow", width=30)
label.pack()

for num, rolename in roles.items():
    Radiobutton(root, text=rolename, variable=var, value=num,
                command=printOption).pack()

root.mainloop()
