"""
Radiobutton

create multiple radiobutton groups

"""

from tkinter import *


def printOption():
    label1.config(text="I am a " + str(var1.get()) + ":"+roles[var1.get()])


def printOption2():
    label2.config(text="I am a " + str(var2.get()) + ":"+races[var2.get()])


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("640x480")

roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
var1 = IntVar()
var1.set(0)

races = {0: 'Human', 1: 'Elf', 2: 'Barbarian'}
var2 = IntVar()
var2.set(0)

label1 = Label(root, text="Please choose a role", bg="lightyellow", width=30)
label1.pack()
for num, rolename in roles.items():
    Radiobutton(root, text=rolename, variable=var1, value=num,
                command=printOption).pack()

label2 = Label(root, text="Please choose a race", bg="lightyellow", width=30)
label2.pack()
for num, racename in races.items():
    Radiobutton(root, text=racename, variable=var2, value=num,
                command=printOption2).pack()

root.mainloop()
