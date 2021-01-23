"""
maximize window
"""

import tkinter as tk
import time

root = tk.Tk()

root.title('Python GUI - Maximize window')

# set init size
w = 800
h = 450

root.geometry(f'{w}x{h}')
print(f'width={root.winfo_width()}, height={root.winfo_height()}')

root.update()
print(f'width={root.winfo_width()}, height={root.winfo_height()}')

time.sleep(2)

# maximise
root.state('zoomed')
root.update()
print(f'width={root.winfo_width()}, height={root.winfo_height()}')

root.mainloop()
