"""
Checkbutton

Registration form
selecting interests
"""

from tkinter import *


def printOption():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get():
            selection += bonus[i] + " "
    print(selection)
    var2.set(selection)


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("360x250+300+300")

label = Label(root, text="Your Interests", bg="lightyellow", width=30, font=("Arial", 18, "bold"))
label.pack()

# data, dictionary
bonus = {0: 'Sports', 1: 'Video Game', 2: 'Reading', 3: 'Fine Art', 4: 'Music'}
checkboxes = {}

for i in range(len(bonus)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=bonus[i], variable=checkboxes[i]).pack()

Button(root, text="OK", width=10, command=printOption).pack()

var2 = StringVar()
var2.set("")

statusbarLabel = Label(root, text="", textvariable=var2, bg="white", anchor="w")
statusbarLabel.pack(fill=X, side="bottom")

root.mainloop()
