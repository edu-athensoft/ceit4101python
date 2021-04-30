"""
set window to the topmost
"""

import tkinter as tk

# init
root = tk.Tk()
root.title('Python GUI - Topmost')
root.geometry('800x450')

# keep on top
root.wm_attributes("-topmost", True)
# root.wm_attributes("-topmost", 1)


# root.attributes("-topmost", True)
# root.attributes("-topmost", 1)

# root.focus_set()

root.mainloop()
