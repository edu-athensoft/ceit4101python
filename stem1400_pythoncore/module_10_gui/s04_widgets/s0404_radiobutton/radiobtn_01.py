"""
Radiobutton

default option selected

"""

from tkinter import *


def printOption():
    label.config(text="I am a " + var.get() + ".")


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("320x120")

var = StringVar()

# set a default selected option
var.set("Warrior")

# select nothing
# var.set(None)

label = Label(root, text="Please choose a role", textvariable=var, bg="lightyellow", width=30)
label.pack()

radiobtn1 = Radiobutton(root, text="Mage", variable=var, value="Mage", command=printOption)
radiobtn1.pack()

radiobtn2 = Radiobutton(root, text="Warrior", variable=var, value="Warrior", command=printOption)
radiobtn2.pack()

radiobtn3 = Radiobutton(root, text="Archer", variable=var, value="Archer", command=printOption)
radiobtn3.pack()

root.mainloop()
