"""
Radiobutton

Registration form
select gender
"""

from tkinter import *


def printOption():
    status_text = "Message: "+var.get() + " selected."
    var2.set(status_text)


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry("360x180+300+300")

var = StringVar()
# select nothing
var.set(None)

label = Label(root, text="Your Gender", bg="lightyellow", width=30, font=("Arial", 18, "bold"))
label.pack()

radiobtn1 = Radiobutton(root, text="Male", variable=var, value="male", command=printOption)
radiobtn1.pack()

radiobtn2 = Radiobutton(root, text="Female", variable=var, value="female", command=printOption)
radiobtn2.pack()

radiobtn3 = Radiobutton(root, text="Not to say", variable=var, value="not_to_say", command=printOption)
radiobtn3.pack()

var2 = StringVar()
var2.set("")

statusbarLabel = Label(root, text="", textvariable=var2, bg="white", anchor="w")
statusbarLabel.pack(fill=X, side="bottom")

root.mainloop()
