"""
Tkinter

place a label widget

anchor= nw, n,    ne
        w,  center,  e
        sw, s,   se

"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label anchor')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Tkinter Label 1',
               height=3, width=40,
               anchor='ne')
label1.pack()

# create a label widget
label2 = Label(root, text='Tkinter Label 2',
               height=7, width=20,
               bg="#ddff33",
               anchor='sw')
label2.pack()


# create a label widget
label3 = Label(root, text='Tkinter Label 3',
               height=7, width=20,
               anchor=CENTER)
label3.pack()

# create a label widget
label4 = Label(root, text='Tkinter Label 3',
               height=7, width=20,
               bg="#ddff33",
               anchor=E)
label4.pack()

root.mainloop()
