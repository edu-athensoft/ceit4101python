"""
tkinter.Pack

Pack.info()

{'in': <tkinter.Tk object .>, 'anchor': 'center', 'expand': 0,
'fill': 'none', 'ipadx': 0, 'ipady': 0, 'padx': 0, 'pady': 0, 'side': 'left'}
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

res = Pack.info(label1)
print(res)


root.mainloop()

