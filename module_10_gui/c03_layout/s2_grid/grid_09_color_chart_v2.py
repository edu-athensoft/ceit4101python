"""
module:     GUI and tkinter
topic:      grid layout
section:    5.2.6 Challenges 2
problem:    color charts
ver:        1
"""

from tkinter import *

root = Tk()
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for index in range(len(colors)):
    Label(root, text=colors[index],
          relief="groove", width=20, padx=20, pady=20,
          font="20").grid(row=index, column=0)

    Label(root, bg=colors[index],
          relief="flat", width=20, padx=20, pady=20).grid(row=index, column=1)

root.mainloop()
