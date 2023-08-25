"""
scrollbar
"""

from tkinter import *

root = Tk()

# create a text widget
text_widget = Text(root, height=10, width=50)

# create a scrollbar and link it to the text widget
scrollbar = Scrollbar(root)
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# pack the scrollbar and text widget
scrollbar.pack(side=RIGHT, fill=Y)
text_widget.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()