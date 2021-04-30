"""
Layout manager:  pack()

option - anchor

"""


from tkinter import *


root = Tk()
root.title('Python GUI - pack anchor')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1 = Label(root, text='< Last', font=('Arial', 20), fg='red')
label2 = Label(root, text='Next >',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Min', font=('Arial', 20), fg='red')
label4 = Label(root, text='Max',bg='yellow', font=('Arial', 20))

label1.pack(anchor=S, side=LEFT)
label2.pack(anchor=S, side=LEFT, padx=10)
label3.pack(anchor=N, side=RIGHT)
label4.pack(anchor=N, side=RIGHT, padx=10)

root.mainloop()

