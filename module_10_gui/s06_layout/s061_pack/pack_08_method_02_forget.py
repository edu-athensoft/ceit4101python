"""
tkinter.Pack

Pack.forget()

"""


from tkinter import *


def hide(widget):
    # print('hide()')
    # it has to return
    # or no response without return statement
    return lambda : Pack.forget(widget)


def show(widget):
    # it has to return
    # or no response without return statement
    return lambda : widget.pack(side = LEFT)


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

label1.after(2000, hide(label1))

# this will do also
# without extra definition of hide
# label1.after(2000, lambda : Pack.forget(label1))

label1.after(3000, show(label1))


root.mainloop()

