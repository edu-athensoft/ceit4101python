"""
Tkinter

compound
text and image

"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label compound')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

#
label1= Label(root, bitmap="question", text="question",
              compound="left")
label1.pack()

#
label2= Label(root, bitmap="info", text="info",
              compound="right")
label2.pack()

#
label3= Label(root, bitmap="warning", text="warning",
              compound="top")
label3.pack()

#
label4= Label(root, bitmap="error", text="error",
              compound="bottom")
label4.pack()

#
label5= Label(root, bitmap="hourglass", text="hourglass",
              compound="center")
label5.pack()

root.mainloop()
