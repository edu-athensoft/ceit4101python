"""
get possible max width and height for a window
"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Maxsize')
root.geometry('800x450+300+200')

# set maxsize
w,h = root.maxsize()
print(f'max_width={w}, max_height={h}')


root.mainloop()