"""
Tkinter

place a label widget

using pack() layout

ref: #1
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label position')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Label position 1',
               height=3, width=40,
               bg='#EF72AA', fg='white')
# show on screen
label1.pack()

# create a label widget
label2 = Label(root, text='Label position 2',
               height=7, width=20,
               bg='#72EFAA', fg='black')
# show on screen
label2.pack()


# create a label widget
label3 = Label(root, text='Label position 3',
               height=3, width=40,
               bg='#EFAA72', fg='white')
# show on screen
label3.pack()



# create a label widget
label1a = Label(root, text='Label position 1',
               height=3, width=40,
               bg='#EF72AA', fg='white')
# show on screen
label1a.pack(side='right')

# create a label widget
label2a = Label(root, text='Label position 2',
               height=7, width=20,
               bg='#72EFAA', fg='black')
# show on screen
label2a.pack()


# create a label widget
label3a = Label(root, text='Label position 3',
               height=3, width=40,
               bg='#EFAA72', fg='white')
# show on screen
label3a.pack(side='left')


root.mainloop()