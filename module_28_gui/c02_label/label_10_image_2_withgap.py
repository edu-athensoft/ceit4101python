"""
Tkinter

place a label widget

image label with .gif


"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label bitmap')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image
bgimg = PhotoImage(file='./pimon.gif')
label1 = Label(root, image=bgimg)

# center on screen
label1.pack()


root.mainloop()