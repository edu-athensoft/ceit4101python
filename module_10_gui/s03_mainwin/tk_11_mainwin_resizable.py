"""
set resizable
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Set resizable')

root.geometry("640x480+200+240")
root.configure(bg='#ddddff')

# set resizable
# option 1.
root.resizable(0,0)         # fixed width and height
# root.resizable(0,1)       # fixed width
# root.resizable(1,0)       # fixed height

# option 2.
# root.resizable(width=False, height=False)
# root.resizable(width=False)
# root.resizable(height=False)


tk.mainloop()