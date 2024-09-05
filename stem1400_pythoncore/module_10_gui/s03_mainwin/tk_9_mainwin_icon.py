"""
set icon for a window
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Main window")

icon_img = 'athens-logo.ico'
root.iconbitmap(icon_img)

root.geometry("640x480+400+300")
root.configure(bg="#ddddff")

root.mainloop()