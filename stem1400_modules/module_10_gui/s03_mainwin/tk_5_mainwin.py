"""
Tkinter

window

get screen width and height
winfo_screenwidth()
winfo_screenheight()

place window at the center of screen

ref: #1
"""


from tkinter import *


root = Tk()
root.title('Python GUI - Center window')

w = 640 # width for the Tk root
h = 480 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))

# set the dimensions of the screen
# and where it is placed
# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.geometry(f'{w}x{h}+{x}+{y}')

root.mainloop()