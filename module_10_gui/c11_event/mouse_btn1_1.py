"""
Event handling
Mouse event
<Button-1>
"""

from tkinter import *


def handler(event):
    position_str = f'clicked at x={event.x},y={event.y}'
    print(position_str)
    var.set(position_str)


root = Tk()
root.title("Python GUI - Event | Mouse")
root.geometry("640x480+300+300")

# label
var = StringVar()
var.set('Move your mouse and click')
label1 = Label(root, textvariable=var, font=("Helvetica",16))
label1.pack(padx=50, pady=10, side=BOTTOM)

# mouse event: Button-1 click
root.bind("<Button-1>", handler)

root.mainloop()
