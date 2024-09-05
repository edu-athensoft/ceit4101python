"""
Key combination

References
https://blog.csdn.net/diaomao5080/article/details/102057248
"""

import tkinter

root = tkinter.Tk()
root.title("Key combination")
root.geometry("800x600+600+100")

label = tkinter.Label(root, text="Please input your key combination")
entry = tkinter.Entry(root)
label.pack()


def func(event):
    print("event.char=", event.char)
    print("event.keysym=",  event.keysym)
    print("event.keycode=", event.keycode)


entry.bind("<Shift-Up>", func)
entry.bind("<Control-a>", func)

# <Shift-Up>
# Control-a
entry.focus_set()  # set focus
entry.pack()

root.mainloop()
