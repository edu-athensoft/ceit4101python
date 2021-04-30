"""
Tkinter

place a label widget

bitmap
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label bitmap')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
# text does not take effect
label1 = Label(root, text='Tkinter Label 1',
               padx=30, pady=20,
               font = "Helnetic 20 bold italic",
               bg='#72EFAA', fg='black',
               bitmap='error')
# show on screen
label1.pack()


# create a label widget
label2 = Label(root, bg='#EF72AA', fg='black', bitmap='question')
# show on screen
label2.pack()




root.mainloop()