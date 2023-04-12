"""
Messagebox

8 modes

"""

from tkinter import *
from tkinter import messagebox


# button response
def msg(type):
    if type == 1:
        print(1)
        messagebox.showinfo('Showinfo', 'This is a showinfo messagebox.')
    elif type == 2:
        print(2)
        messagebox.showwarning('Showwarning', 'This is a showwarning messagebox.')
    elif type == 3:
        print(3)
        messagebox.showerror('Showerror', 'This is a showerror messagebox.')
    elif type == 4:
        print(4)
        # return yes or no
        decision = messagebox.askquestion('Askquestion', 'This is a askquestion messagebox.')
        print(decision)
    elif type == 5:
        print(5)
        # return True or False
        decision = messagebox.askokcancel('Askokcancel', 'This is a askokcancel messagebox.')
        print(decision)
    elif type == 6:
        print(6)
        # return True or False
        decision = messagebox.askyesno('Askyesno', 'This is a askyesno messagebox.')
        print(decision)
    elif type == 7:
        print(7)
        # return True , False or None
        decision = messagebox.askyesnocancel('Askyesnocancel', 'This is a askyesnocancel messagebox.')
        print(decision)
    elif type == 8:
        print(8)
        # return True or False
        decision = messagebox.askretrycancel('Askretrycancel', 'This is a askretrycancel messagebox.')
        print(decision)
    else:
        print('no such type')


# main program
root = Tk()
root.title("Python GUI - Spinbox")
root.geometry("360x240")
root.config(bg="#ddddff")

# button widget
Button(root, text='Showinfo 1', command=lambda: msg(1)).pack()
Button(root, text='Showwarning 2', command=lambda: msg(2)).pack()
Button(root, text='Showerror 3', command=lambda: msg(3)).pack()
Button(root, text='Askquestion 4', command=lambda: msg(4)).pack()
Button(root, text='Askokcancel 5', command=lambda: msg(5)).pack()
Button(root, text='Askyesno 6', command=lambda: msg(6)).pack()
Button(root, text='Askyesnocancel 7', command=lambda: msg(7)).pack()
Button(root, text='Askretrycancel 8', command=lambda: msg(8)).pack()

# messagebox widget


root.mainloop()
