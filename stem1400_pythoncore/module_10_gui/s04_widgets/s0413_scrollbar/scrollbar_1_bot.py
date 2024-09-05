"""
scrollbar
"""

import tkinter as tk

root = tk.Tk()

# create a text widget
text_widget = tk.Text(root, height=10, width=50)

# create a scrollbar and link it to the text widget
scrollbar = tk.Scrollbar(root)
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# pack the scrollbar and text widget
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()