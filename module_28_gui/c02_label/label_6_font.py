"""
Tkinter

place a label widget

Font
family:     Helvetica,Times, etc
size:       in px
weight:     bold,normal
slant:      italic,roman
underline:  True,False
overstrike: True,False
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label font')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='Tkinter Label 1',
               height=3, width=28,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black')
# show on screen
label1.pack()

# create a label widget
label2 = Label(root, text='Tkinter Label 2',
               height=3, width=20,
               font = ("Times", 16, "normal", "roman"))
# show on screen
label2.pack()


# create a label widget
label3 = Label(root, text='Tkinter Label 3',
               height=3, width=20,
               font = ("Helnetic", 24, "underline", "bold", "roman"),
               bg='#EF72AA', fg='white')
# show on screen
label3.pack()

# create a label widget
label4 = Label(root, text='Tkinter Label 4',
               height=3, width=20,
               font = ("Helnetic", 18, "overstrike", "normal", "roman"),
               bg='#72AAEF', fg='white')
# show on screen
label4.pack()

# create a label widget
label4 = Label(root, text='Tkinter Label 5',
               height=3, width=20,
               font = ("Helnetic", 18, "overstrike", "underline", "normal", "roman"),
               bg='#72EFAA', fg='black')
# show on screen
label4.pack()

root.mainloop()