"""
Tkinter

place a label widget

bitmap

display all built-in bitmaps
"""


from tkinter import *


root = Tk()

root.title('Python GUI - Label bitmap')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

label1 = Label(root, bitmap='error')
label2 = Label(root, bitmap='hourglass')
label3 = Label(root, bitmap='info')
label4 = Label(root, bitmap='questhead')
label5 = Label(root, bitmap='question')
label6 = Label(root, bitmap='warning')
label7 = Label(root, bitmap='gray12')
label8 = Label(root, bitmap='gray25')
label9 = Label(root, bitmap='gray50')
label10 = Label(root, bitmap='gray75')


# display labels
for i in range(1, 11):
    obj = 'label' + str(i)
    eval(obj).pack()

# eval() allows to refer to the object by name

root.mainloop()