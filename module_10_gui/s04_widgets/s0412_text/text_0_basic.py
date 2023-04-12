"""
text

basic Text widget
"""

from tkinter import *
from tkinter.ttk import Separator



root = Tk()
root.title("Athensoft Python Course | Text")
root.geometry("640x480+300+300")

# text widget
text = Text(root, height = 5, width = 30)
# text.pack(fill=BOTH, expand=Y)
text.pack()

# init text
# text.insert(END, "Python\nTkinter\n")
# text.insert(END, "I like you.")


root.mainloop()