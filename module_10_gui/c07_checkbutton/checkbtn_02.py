"""
Checkbutton

get()
dictionary
variable, BooleanVar()
"""

from tkinter import *


def printInfo():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += bonus[i] + "\t"
    print(selection)


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x180")

# label
label = Label(root, text="Please choose your bonus", bg="lightyellow", width=30)
label.pack()

# data, dictionary
bonus = {0: 'Weapon', 1: 'Diamond', 2: 'Skill'}
checkboxes = {}

for i in range(len(bonus)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=bonus[i], variable=checkboxes[i]).pack()

Button(root, text="OK", width=10, command=printInfo).pack()

root.mainloop()
