"""
update window's current status
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Update')
root.configure(bg='#ddddff')

root.geometry("{}x{}+200+240".format(640, 480))
print(f'Initial window width={root.winfo_width()} and height={root.winfo_height()}')

root.update()
print(f'Current window width={root.winfo_width()} and height={root.winfo_height()}')

tk.mainloop()