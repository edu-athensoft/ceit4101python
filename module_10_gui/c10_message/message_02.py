"""
Message

similar to Label

aspect
- of width/height
- number of width/height without percentage sign
- default 150, w:h = 1.5: 1

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Message")
root.geometry("360x240")
root.config(bg="#ddddff")

# message widget
Message(root, text='hello Message Message', aspect=400).pack()
Message(root, text='hello Message Message').pack(pady=10)


root.mainloop()
