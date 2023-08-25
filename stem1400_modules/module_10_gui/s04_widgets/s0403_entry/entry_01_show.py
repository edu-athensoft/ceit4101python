"""
Entry

padx(left, right)
width

"""

from tkinter import *


def showPwd():
    print("showPwd()")
    entryObj = passwordE
    # entryObj['show']='??'
    entryObj['show']=''
    # entryObj['text']=entryObj.get()
    # print(entryObj.get())
    root.update()


def hidePwd():
    print("hidePwd()")
    entryObj = passwordE
    entryObj['show']='*'
    # entryObj['text']=entryObj.get()
    # print(entryObj.get())
    root.update()


root = Tk()
root.title("Python GUI - Entry")
root.geometry("300x160")

accountL = Label(root, text="Account ")
accountL.grid(row=2,padx=(50,5), sticky='e')

passwordL = Label(root, text="Password ")
passwordL.grid(row=3,padx=(50,5), sticky='e')

accountE = Entry(root)
accountE.grid(row=2, column=1, padx=(5, 50))

passwordE = Entry(root, show='*')
passwordE.grid(row=3, column=1, padx=(5, 50))

showBtn = Button(root, text='Show password', command=showPwd)
showBtn.grid(row=4, column=1)

showBtn = Button(root, text='Hide password', command=hidePwd)
showBtn.grid(row=5, column=1)

root.mainloop()
