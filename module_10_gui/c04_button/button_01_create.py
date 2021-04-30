"""
Button

1. command and callback function
2. exit GUI program, closing window

"""
from tkinter import *


def msgShow():
    label["text"] = "Button Widget"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    label.config(text="Athensoft Python Course", bg="lightyellow", fg="blue")


root = Tk()
root.title("Python GUI - Athensoft")

# widget
label = Label(root)
btn1 = Button(root, text="Show Message", width=15, command=msgShow)
btn2 = Button(root, text="Exit", width=15, command=root.destroy)

# layout
label.grid(row=0, column=0, columnspan=2)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)

root.mainloop()
