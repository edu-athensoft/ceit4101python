"""
Tkinter

place a label widget

padx, pady
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label justify')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Tkinter Label 1',
               padx=30, pady=20,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               wraplength=180,
               justify='right')
# show on screen
label1.pack()


# create a label widget
label2 = Label(root, text='Tkinter Label 2',
               padx=15, pady=10,
               font = "Helnetic 20 bold italic",
               bg='#EF72AA', fg='black',
               wraplength=180,
               justify='left')
# show on screen
label2.pack()


# create a label widget
label3 = Label(root, text='Tkinter Label 3',
               padx=10, pady=5,
               font = "Helnetic 20 bold italic",
               bg='#EFAA72', fg='black',
               wraplength=180,
               justify='center')
# show on screen
label3.pack()

root.mainloop()