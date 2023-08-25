"""
Layout manager:  pack()

padx, pady

"""


from tkinter import *


root = Tk()
root.title('Python GUI - Layout pack')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1 = Label(root, text='Python', font=('Arial', 20))
label2 = Label(root, text='Java',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web', font=('Arial', 20))
label4 = Label(root, text='Database',bg='yellow', font=('Arial', 20))

label1.pack(side=LEFT, padx=20)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)

root.mainloop()

