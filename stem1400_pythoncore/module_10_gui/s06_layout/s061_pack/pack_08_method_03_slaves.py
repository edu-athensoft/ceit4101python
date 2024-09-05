"""
tkinter.Pack

Pack.slaves(parent_object)

[<tkinter.Label object .!label>,
<tkinter.Label object .!label2>,
<tkinter.Label object .!label3>]
"""


from tkinter import *

root = Tk()
root.title('Python GUI - pack fill')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label1 = Label(root, text='Java 1', font=('Arial', 20), fg='red')
label2 = Label(root, text='Python 2',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web 3', font=('Arial', 20), fg='red')

label1.pack(side = LEFT)
label2.pack(side = LEFT)
label3.pack(side = LEFT)

res = Pack.slaves(root)
print(res)


root.mainloop()

