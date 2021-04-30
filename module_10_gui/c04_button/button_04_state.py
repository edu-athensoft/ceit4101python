"""
Button

and set state for a button
state = {active, disabled, normal}
"""


from tkinter import *


root = Tk()
root.geometry("320x240+200+200")
root.config(bg="#ddddff")
root.title("Python GUI - Button State")

btn1 = Button(root, text='Default State')
btn1.pack()

# the state must be active, disabled, or normal
btn2 = Button(root, text='Active State', state='active')
btn2.pack()

btn3 = Button(root, text='Disabled State', state='disabled')
btn3.pack()

btn4 = Button(root, text='Normal State', state='normal')
btn4.pack()

root.mainloop()