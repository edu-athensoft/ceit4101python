"""
project name: calculator

chapter: GUI tkinter
section: Entry
"""
from tkinter import *


def calculate():
    r = re.findall(".+", equ.get())
    result = eval(str(r[-1]))
    equ.set(equ.get() + "\n" + str(result))


def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)


def backspace():
    equ.set(str(equ.get()[:-1]))


def clear():
    equ.set("0")


# main program
root = Tk()
root.title("Python GUI - Calculator")

equ = StringVar()
equ.set("0")  # default display value = 0

# display
label = Label(root, width=44, height=2, relief="raised", anchor=SE, textvariable=equ, font=(22))
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# buttons
Button(root, text="C", fg="blue", width=10, command=clear, font=(18)).grid(row=1, column=0)
Button(root, text="DEL", width=10, command=backspace, font=(18)).grid(row=1, column=1)
Button(root, text="%", width=10, command=lambda: show("%"), font=(18)).grid(row=1, column=2)
Button(root, text="/", width=10, command=lambda: show("/"), font=(18)).grid(row=1, column=3)

Button(root, text="7", width=10, command=lambda: show("7"), font=(18)).grid(row=2, column=0)
Button(root, text="8", width=10, command=lambda: show("8"), font=(18)).grid(row=2, column=1)
Button(root, text="9", width=10, command=lambda: show("9"), font=(18)).grid(row=2, column=2)
Button(root, text="*", width=10, command=lambda: show("*"), font=(18)).grid(row=2, column=3)

Button(root, text="4", width=10, command=lambda: show("4"), font=(18)).grid(row=3, column=0)
Button(root, text="5", width=10, command=lambda: show("5"), font=(18)).grid(row=3, column=1)
Button(root, text="6", width=10, command=lambda: show("6"), font=(18)).grid(row=3, column=2)
Button(root, text="-", width=10, command=lambda: show("-"), font=(18)).grid(row=3, column=3)

Button(root, text="1", width=10, command=lambda: show("1"), font=(18)).grid(row=4, column=0)
Button(root, text="2", width=10, command=lambda: show("2"), font=(18)).grid(row=4, column=1)
Button(root, text="3", width=10, command=lambda: show("3"), font=(18)).grid(row=4, column=2)
Button(root, text="+", width=10, command=lambda: show("+"), font=(18)).grid(row=4, column=3)

Button(root, text="0", width=21, command=lambda: show("0"), font=(18)).grid(row=5, column=0, columnspan=2)
Button(root, text=".", width=10, command=lambda: show("."), font=(18)).grid(row=5, column=2)
Button(root, text="=", bg="lightyellow", width=10, command=calculate, font=(18)).grid(row=5, column=3)

root.mainloop()
