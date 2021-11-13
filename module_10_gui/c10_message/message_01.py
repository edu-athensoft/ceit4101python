"""
Message

similar to Label

comparing with label

"""

from tkinter import *

root = Tk()
root.title("Python GUI - Spinbox")
root.geometry("360x240")
root.config(bg="#ddddff")

# message widget
Message(root, text='hello Message').pack()
Message(root, text='hello Message Message').pack(pady=10)

# label widget
Label(root, text='hello Label Label').pack(pady=10)

root.mainloop()
