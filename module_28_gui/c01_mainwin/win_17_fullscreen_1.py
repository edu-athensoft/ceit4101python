"""
get possible max width and height for a window
"""

import tkinter as tk

def fullscreen():
    # set full screen
    root.attributes('-fullscreen', True)


def quitfullscreen():
    root.attributes('-fullscreen', False)
    # root.update()


def quitscreen():
    root.quit()


# init
root = tk.Tk()
root.title('Python GUI - Fullscreen')
root.geometry('800x450')

btn1 = tk.Button(root, text='FullScreen', padx=30, pady=20, command=fullscreen)
btn1.pack()

btn2 = tk.Button(root, text='Exit FullScreen', padx=30, pady=20, command=quitfullscreen)
btn2.pack()

btn2 = tk.Button(root, text='Close Screen', padx=30, pady=20, command=quitscreen)
btn2.pack()


# root.wm_attributes("-topmost", 1) # keep on top
# root.focus_set()

# root.bind("<Escape>", lambda event:root.destroy())
root.bind("<Escape>", lambda event:root.quit())
root.bind("<F11>", lambda event: fullscreen())
root.bind("<F12>", lambda event: quitfullscreen())

root.mainloop()