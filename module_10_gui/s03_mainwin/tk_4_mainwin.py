"""
Tkinter

create a main window

set dimension or size
set init position

ref: #1
"""


from tkinter import *


root = Tk()
root.title('Python GUI - main window')

# root.geometry('640x480+20+20')

root.geometry('640x480+0+0')

# root.geometry('640x480-5+0')

# anti
# root.geometry('640X480')  # error

root.mainloop()