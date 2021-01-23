"""
destroy a window

destroy()
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Update')
root.configure(bg='#ddddff')

root.geometry("{}x{}+200+240".format(640, 480))
print(f'Press button to destroy the window.')

btn1 = tk.Button(root, text="Destroy this window", command=root.destroy)
btn1.pack()

tk.mainloop()

print(f'The window has been destroyed.')

root.destroy()



