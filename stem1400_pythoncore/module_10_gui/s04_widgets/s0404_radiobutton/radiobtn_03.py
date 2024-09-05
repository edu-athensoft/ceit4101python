"""
Radiobutton

create multiple radiobutton groups

"""

from tkinter import *


def printOption():
    label1.config(text="I am a " + var1.get() + ".")


def printOption2():
    label2.config(text="I am a " + var2.get() + ".")


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480")

var1 = StringVar()
var1.set(None)

label1 = Label(root, text="Please choose a role", bg="lightyellow", width=30)
radiobtn1a = Radiobutton(root, text="Mage", variable=var1, value="Mage", command=printOption)
radiobtn1b = Radiobutton(root, text="Warrior", variable=var1, value="Warrior", command=printOption)
radiobtn1c = Radiobutton(root, text="Archer", variable=var1, value="Archer", command=printOption)

var2 = StringVar()
var2.set(None)

label2 = Label(root, text="Please choose a race", bg="lightyellow", width=30)
radiobtn2a = Radiobutton(root, text="Human", variable=var2, value="Human", command=printOption2)
radiobtn2b = Radiobutton(root, text="Elf", variable=var2, value="Elf", command=printOption2)
radiobtn2c = Radiobutton(root, text="Barbarian", variable=var2, value="Barbarian", command=printOption2)

label2.pack()
radiobtn2a.pack()
radiobtn2b.pack()
radiobtn2c.pack()

label1.pack()
radiobtn1a.pack()
radiobtn1b.pack()
radiobtn1c.pack()

root.mainloop()
