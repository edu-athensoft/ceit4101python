"""
Button

Volume controller

and set state for a button
state = {active, disabled, normal}
"""

from tkinter import *


def add(step=1):
    global value
    value += step
    if value >= MAX:
        btn1.config(state='disabled')
        btn2.config(state='active')
    else:
        btn1.config(state='active')
        btn2.config(state='disabled')
    label_num.config(text=str(value))



def sub(step=1):
    global value
    value -= step
    if value <= MIN:
        btn2.config(state='disabled')
        btn1.config(state='active')
    else:
        btn2.config(state='active')
        btn1.config(state='disabled')
    label_num.config(text=str(value))


root = Tk()
root.title("Python GUI - Button")
root.geometry("300x200")
root.config(bg='#ddddff')

# create 3 buttons
btn1 = Button(root, text="+", padx=25, font=(None, 16, 'bold'), command=lambda:add(2))
btn2 = Button(root, text="-", padx=25, font=(None, 16, 'bold'), command=lambda:sub(2))
btn_exit = Button(root, text="Exit", padx=25, font=(None, 16), command=root.destroy)

# label of number
value = 0
MAX = 10
MIN = -10
label_num = Label(root, text=str(value), font=(None,40), pady=50)

#
label_num.pack(fill=X)
btn_exit.pack(anchor=S, side=RIGHT, padx=5, pady=5)
btn1.pack(anchor=S, side=RIGHT, padx=5, pady=5)
btn2.pack(anchor=S, side=RIGHT, padx=5, pady=5)

root.mainloop()
