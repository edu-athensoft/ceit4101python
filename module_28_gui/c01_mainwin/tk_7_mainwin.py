"""
center window
set as max window
"""

import tkinter as tk


def max_window():
    w, h = root.maxsize()
    root.geometry("{}x{}".format(w, h))


def min_window(w, h):
    res = root.minsize()
    print(res)
    root.geometry("{}x{}+200+200".format(res[0], res[1]))


root = tk.Tk()
root.title('Python GUI - Maximize window')
max_window()

w= 120
h= 90
# min_window(w, h)
max_window()
root.mainloop()