"""
set max width and height for a window by user
"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Maxsize')
root.geometry('800x450+300+200')

# set maxsize
root.maxsize(1200,675)


root.mainloop()