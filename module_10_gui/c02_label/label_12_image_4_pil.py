"""
Tkinter

label of Image
display a jpg
"""


from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('Python GUI - Label image with PIL')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in jpg
bgimg = Image.open('./img/dog3.jpg')
jpg_bgimg = ImageTk.PhotoImage(bgimg)
label1 = Label(root, image=jpg_bgimg)

label1.pack()

root.mainloop()
