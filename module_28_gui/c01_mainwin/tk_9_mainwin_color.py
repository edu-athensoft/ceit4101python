"""
set background color
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Background color')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
root.configure(bg='#DDDDFF')
root.configure(bg='SeaGreen')
root.configure(bg='Tomato')
root.configure(bg='Gold')

tk.mainloop()