"""
Layout manager:  pack()

side
mix

"""


from tkinter import *


root = Tk()

label1 = Label(root, text='Python 1', font=(40))
label2 = Label(root, text='Java 2',bg='yellow', font=(40))
label3 = Label(root, text='Web 3', font=(40))
label4 = Label(root, text='Database 4',bg='yellow',font=(40))

root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1.pack(side=BOTTOM)
label2.pack(side=RIGHT)
label3.pack(side=LEFT)
# label3.pack(side=RIGHT)
label4.pack(side=TOP)

root.mainloop()

