"""
Event handling
Keyboard event
<FocusIn>
<FocusOut>
"""

from tkinter import *


def handle_focusin(x):
    print(f"FocusIn event came from {x} - {eval(x).focus_get()}")


def handle_focusout(x):
    print(f"FocusOut event came from {x} - {eval(x).focus_get()}")


root = Tk()
root.title("Python GUI - Event | Keyboard")
root.geometry("360x180+300+300")
root.config(bg="#ddddff")

# labels and entries
e1 = Entry(root)
e2 = Entry(root)
label1 = Label(root, text='Entry1')
label2 = Label(root, text='Entry2')

label1.grid(row=0,column=0, padx=(50,5), pady=(30,0))
label2.grid(row=1,column=0, padx=(50,5))
e1.grid(row=0,column=1, pady=(30,0))
e2.grid(row=1,column=1)

# keyboard event
e1.bind("<FocusIn>", lambda x: handle_focusin("label1"))
e1.bind("<FocusOut>", lambda x: handle_focusout("label1"))

e2.bind("<FocusIn>", lambda x: handle_focusin("label2"))
e2.bind("<FocusOut>", lambda x: handle_focusout("label2"))

root.mainloop()
