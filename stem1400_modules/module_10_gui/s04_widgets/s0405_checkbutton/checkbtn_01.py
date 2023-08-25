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
        if checkboxes[i].get():
            selection += roles[i] + ", "
    print(selection)

    # print checkboxes
    for i in checkboxes:
        print(f"{i}:{checkboxes.get(i)}")

    for i in checkboxes:
        print(f"{i}:{checkboxes.get(i).get()}")


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x180")

# label
label = Label(root, text="Please choose your roles", bg="lightyellow", width=30)
label.pack()

# data, dictionary
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}
checkboxes[0] = BooleanVar()
checkboxes[1] = BooleanVar()
checkboxes[2] = BooleanVar()
checkBtn1 = Checkbutton(root, text=roles[0], variable=checkboxes[0])
checkBtn2 = Checkbutton(root, text=roles[1], variable=checkboxes[1])
checkBtn3 = Checkbutton(root, text=roles[2], variable=checkboxes[2])

btn = Button(root, text="OK", width=10, command=printInfo)

checkBtn1.pack()
checkBtn2.pack()
checkBtn3.pack()
btn.pack()

root.mainloop()
