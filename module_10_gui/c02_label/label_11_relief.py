"""
Tkinter

label relief

flat
groove
raised
ridge
solid
sunken

"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label justify')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Tkinter Label flat',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               relief='flat')
label1.pack()

# create a label widget
label2 = Label(root, text='Tkinter Label groove',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72AAEF', fg='black',
               relief='groove')
label2.pack()

# create a label widget
label3 = Label(root, text='Tkinter Label raised',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               relief='raised')
label3.pack()


# create a label widget
label4 = Label(root, text='Tkinter Label ridge',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72AAEF', fg='black',
               relief='ridge')
label4.pack()

# create a label widget
label5 = Label(root, text='Tkinter Label solid',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               relief='solid')
label5.pack()

# create a label widget
label6 = Label(root, text='Tkinter Label sunken',
               padx=30, pady=15,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               relief='sunken')
label6.pack()

root.mainloop()
