"""
Tkinter

place a label widget

image label with .gif


"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label image')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image
bgimg = PhotoImage(file='img/pimon.gif')
label1 = Label(root, image=bgimg)

# center on screen
label1.pack(fill=X,padx=10,pady=5)

root.mainloop()
