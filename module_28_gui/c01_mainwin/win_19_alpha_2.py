"""
test alpha visual effect
"""

import tkinter as tk
import time

# init
root = tk.Tk()
root.title('Python GUI - Topmost')
root.geometry('800x450')

# set alpha value
alpha = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]

for i in alpha:
    time.sleep(0.2)
    root.wm_attributes("-alpha", i)
    root.update()


root.mainloop()
