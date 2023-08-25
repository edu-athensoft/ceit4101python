from tkinter import *

top = Tk()

top.geometry("800x600")

# creating a simple canvas
c = Canvas(top, bg="pink", width="800", height="600")

c.pack()

top.mainloop()