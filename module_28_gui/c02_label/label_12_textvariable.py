"""
Tkinter

place a label widget

textvariable
"""


from tkinter import *
import time

root = Tk()

root.title('Python GUI - Label textvariable')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# define variable in tkinter
v = StringVar()

# using set() to set text
v.set("Initial text")

# adding variable text
label_1 = Label(root, textvariable=v, bg="seagreen", fg="white", font=("Times", 40))
label_1.pack()

try:
    while True:
        v.set("%s" % time.ctime())
        label_1.update()
        time.sleep(1)
except Exception as e:
    print(e)

root.mainloop()