"""
get possible min width and height for a window
"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Minsize')
root.geometry('800x450+300+200')

# set minsize
w,h = root.minsize()
print(f'max_width={w}, max_height={h}')


root.mainloop()