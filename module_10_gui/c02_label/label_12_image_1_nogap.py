"""
Tkinter

place a label widget

image label with .gif, .png

"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label image')

# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in .gif
bgimg = PhotoImage(file='./img/pimon.gif')
label1 = Label(root, image=bgimg)
label1.pack()


root.mainloop()
