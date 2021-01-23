"""
get possible max width and height for a window
"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Maxsize')

# get maxsize
w, h = root.maxsize()
root.geometry(f'{w}x{h}')

print(f'max_width={w}, max_height={h}')


root.mainloop()