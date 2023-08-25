"""
Tkinter

create a main window

set dimension or size

radio w:h
3:2
4:3
16:9
16:10

ref: #1
"""


from tkinter import *


root = Tk()
root.title('Python GUI - main window')

root.geometry('640x480')

# anti
# root.geometry('640X480')  # error

root.mainloop()