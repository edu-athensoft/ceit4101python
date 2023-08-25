"""
text

Font family
"""

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from tkinter.ttk import Style
from tkinter.font import Font


def countlines(event):
    (line, c) = map(int, event.widget.index("end-1c").split("."))
    # print(line, c)
    status_text1 = f"Status: INSERT MODE  ROW:{line},COL:{c}"
    var.set(status_text1)


def func1():
    str_status = var.get()
    status_text2 = ' ' * 5 + "Open was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''


def func2():
    str_status = var.get()
    status_text2 = ' ' * 5 + "Save was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''


def func3():
    str_status = var.get()
    status_text2 = ' ' * 5 + "Copy was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''
    copy()


def func4():
    str_status = var.get()
    status_text2 = ' ' * 5 + "Cut was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''
    cut()


def func5():
    str_status = var.get()
    status_text2 = ' ' * 5 + "Paste was called."
    var.set(status_text1 + status_text2)
    status_text2 = ''
    paste()


def newfile():
    messagebox.showinfo("File", "New File")


def openfile():
    messagebox.showinfo("File", "New File")


def save():
    messagebox.showinfo("File", "New File")


def saveas():
    messagebox.showinfo("File", "New File")


def copy():
    try:
        text.clipboard_clear()  # clear clipboard
        copyText = text.get(SEL_FIRST, SEL_LAST)
        text.clipboard_append(copyText)
    except TclError:
        print("Nothing selected")


def cut():
    copy()
    text.delete(SEL_FIRST, SEL_LAST)


def paste():
    try:
        copyText = text.clipboard_get()
        if len(copyText) != 0:
            text.insert(INSERT, copyText)
    except:
        print("No data in clipboard")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


def change_fontfamily(event):
    f = Font(family=familyVar.get())
    text.configure(font=f)


root = Tk()
root.title("Athensoft Python Course | My Text Editor")
root.geometry("640x480+300+300")
icon_img = 'athensoft16.ico'
root.iconbitmap(icon_img)

# main menu
menubar = Menu(root)

# main menu item - file
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# level 2 menu options
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open File", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)


# main menu item - edit
editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=editmenu)
# level 2 menu options
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Paste", command=paste)

# set menu to window
root.config(menu=menubar)

# =================================

# popup menu
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Copy", command=copy)
popupmenu.add_command(label="Cut", command=cut)
popupmenu.add_separator()
popupmenu.add_command(label="Paste", command=paste)

# binding to root
root.bind("<Button-3>", showPopupMenu)


# =================================


# toolbar frame
frame_toolbar = Frame(root, height=30)
frame_toolbar.pack(anchor=W)

btn1 = Button(frame_toolbar, text='Open', command=func1, relief='flat')
btn1.pack(side=LEFT)

btn2 = Button(frame_toolbar, text='Save', command=func2, relief='flat')
btn2.pack(side=LEFT)

btn3 = Button(frame_toolbar, text='Copy', command=func3, relief='flat')
btn3.pack(side=LEFT)

btn4 = Button(frame_toolbar, text='Cut', command=func4, relief='flat')
btn4.pack(side=LEFT)

btn5 = Button(frame_toolbar, text='Paste', command=func5, relief='flat')
btn5.pack(side=LEFT)


# s = Style()
# s.configure("TMenubutton", background="red")


familyVar = StringVar()
familyFamily = ("", "Arial", "Times", "Courier")
familyVar.set(familyFamily[1])
family = OptionMenu(frame_toolbar, familyVar, *familyFamily, command = change_fontfamily)
family.pack(side = LEFT, pady = 5)

family.config(relief='flat')
# =================================

# textarea frame
frame_text = Frame(root, height=30)
frame_text.pack(anchor=CENTER, fill=BOTH, expand=Y)

# text widget
text = Text(frame_text, height=5, width=30)
text.pack(side=LEFT, fill=BOTH, expand=Y)

# init text
# text.insert(END, "Python\nTkinter\n")
# text.insert(END, "I like you.")

# scrollbar
yscrollbar = Scrollbar(frame_text)
yscrollbar.pack(side=RIGHT, fill=Y)
yscrollbar.config(command=text.yview)
text.config(yscrollcommand=yscrollbar.set)

# listening
text.bind("<KeyRelease>", countlines)

# textarea frame
frame_status = Frame(root)
frame_status.pack(anchor=CENTER, fill=X)

# separator
sep = Separator(frame_status, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# status bar
var = StringVar()

# for mode and position
status_text1 = "Status: INSERT MODE"

statusbar = Label(frame_status, textvariable=var)
statusbar.pack(side=BOTTOM, anchor=S + W)
var.set(status_text1)

# for function button clicked
status_text2 = ""

root.mainloop()
