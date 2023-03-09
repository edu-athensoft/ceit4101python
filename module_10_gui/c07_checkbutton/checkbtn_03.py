"""
Checkbutton

option: onvalue
"""

from tkinter import *


def printInfo():
    print(var1.get(), var2.get(), var3.get())


# main program
root = Tk()
root.title("Python GUI - Checkbutton")
root.geometry("320x180")

# label
label = Label(root, text="Please choose your roles", bg="lightyellow", width=30)
label.pack()

# data, dictionary
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
checkBtn1 = Checkbutton(root, text=roles[0], onvalue=1, offvalue=0, variable=var1)
checkBtn2 = Checkbutton(root, text=roles[1], onvalue=1, offvalue=0, variable=var2)
checkBtn3 = Checkbutton(root, text=roles[2], onvalue=1, offvalue=0, variable=var3)

btn = Button(root, text="OK", width=10, command=printInfo)

checkBtn1.pack()
checkBtn2.pack()
checkBtn3.pack()
btn.pack()

root.mainloop()
