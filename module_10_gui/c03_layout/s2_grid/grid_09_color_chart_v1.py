"""
module:     GUI and tkinter
topic:      grid layout
section:    5.2.6 Challenges 1
problem:    color charts
ver:        1
"""

from tkinter import *

root = Tk()
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

# initial row number
r = 0

for color in colors:
    Label(root, text=color,
          relief="groove", width=20, padx=20, pady=20,
          font="20").grid(row=r, column=0)

    Label(root, bg=color,
          relief="flat", width=20, padx=20, pady=20).grid(row=r, column=1)

    r += 1

root.mainloop()
