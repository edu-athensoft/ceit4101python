"""
get possible max width and height for a window
"""

import tkinter as tk

root = tk.Tk()

root.title('Python GUI - Maxsize')

# get maxsize
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
# root.overrideredirect(True)
root.overrideredirect(1)
root.geometry(f'{w}x{h}+0+0')


root.geometry(f'{400}x{500}+0+0')
print(f'max_width={w}, max_height={h}')


root.mainloop()