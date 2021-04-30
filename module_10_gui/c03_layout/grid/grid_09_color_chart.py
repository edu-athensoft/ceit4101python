"""
Tkinter

using grid layout

color charts
"""


from tkinter import *


root = Tk()
# root.geometry('640x480+200+200')
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Grid')

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]

# initial row number
r = 0

for color in colors:
    Label(root, text = color,
          relief="groove", width = 20, padx=20, pady=20,
          font="20").grid(row=r, column=0)

    Label(root, bg = color,
          relief="flat", width = 20, padx=20, pady=20).grid(row=r, column=1)

    r += 1

root.mainloop()
