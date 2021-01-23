"""
set window to the topmost
"""

import tkinter as tk

# init
root = tk.Tk()
root.title('Python GUI - Topmost')
root.geometry('800x450')

# set alpha value
# alpha = 0.25
# alpha = 0.5
alpha = 0.75
# alpha = 1
root.wm_attributes("-alpha", alpha)


root.mainloop()
