"""
set window in full screen mode and toggle
"""

from tkinter import *


class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        # only work at Linux
        # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        # self.tk.attributes('-zoomed', True)
        self.tk.title('Python GUI - Fullscreen Toggle - OOP')
        self.tk.geometry('800x450')
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()
