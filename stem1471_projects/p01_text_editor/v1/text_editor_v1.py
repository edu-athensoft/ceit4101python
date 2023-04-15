"""
Athensoft Python Course Project
Project: My Text Editor
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Separator


# settings
BRAND_TITLE = "Athensoft Text Editor - "
CURRENT_EDIT_STATUS = "UNSAVED"
DEFAULT_FILE = "untitled.txt"
BASE_PATH = "C:\\Users\\Athens\\Desktop\\python_demo\\"
CURRENT_FILE = BASE_PATH + DEFAULT_FILE
ICON_LOGO = "athensoft16.ico"
ICON_ARROW = 'arrow.png'

# file functions
def newfile():
    global CURRENT_FILE
    global CURRENT_EDIT_STATUS

    if CURRENT_EDIT_STATUS == 'UNSAVED':
        messagebox.showinfo("File", "Please save your current file!")
        return
    else:
        # clear current textarea
        print("ready to new file...")

        CURRENT_FILE= BASE_PATH + DEFAULT_FILE
        CURRENT_EDIT_STATUS = 'UNSAVED'

        # update title
        root.title(BRAND_TITLE+CURRENT_FILE)

        if text.get("1.0","end"):
            # clear text area
            text.delete("1.0","end")

            # change status
            status_text2 = ' ' * 5 + CURRENT_EDIT_STATUS
            var.set(status_text1 + status_text2)


def openfile():
    # choose file with filechooser
    filename = filedialog.askopenfilename()
    if filename.strip() == '':
        messagebox.showinfo("File", "No file was selected.")
        return

    # set current title
    global CURRENT_FILE
    CURRENT_FILE = filename
    root.title(BRAND_TITLE+filename)

    # open and read file
    print("opening...")
    text.delete("1.0","end")
    with open(filename) as f:
        content = f.readlines()
        f.close()
    print("opened.")

    # change status
    status_text2 = ' ' * 5 + "opened."
    var.set(status_text1 + status_text2)

    # show text in textarea
    for line in content:
        text.insert(END, line)


def save():
    # save to current file
    print("saving...")
    filename = CURRENT_FILE
    content=text.get("1.0","end")
    with open(filename,'w') as f:
        f.write(content)
        f.close()
    print('saved.')

    # update status
    global CURRENT_EDIT_STATUS
    CURRENT_EDIT_STATUS = 'SAVED'

    status_text2 = ' ' * 5 + CURRENT_EDIT_STATUS
    var.set(status_text1 + status_text2)

    # show message
    messagebox.showinfo("File", f'{filename} is saved.')


def saveas():
    fileName = ''

    def confirmName():
        nonlocal fileName
        fileName = fileNameE.get()

        # adding file extension if necessary
        if fileName.count('.') == 0:
            fileName += '.txt'
        print(fileName)

        # change title
        global CURRENT_FILE
        CURRENT_FILE = BASE_PATH + fileName
        root.title(BRAND_TITLE+fileName)

        # save and close dialog
        save()
        topframe.destroy()

    # file name dialog
    topframe = Toplevel()
    topframe.geometry("300x180+1400+155")
    topframe.title("Save as")

    fileFrame = Frame(topframe)
    fileFrame.pack()

    fileNameL = Label(fileFrame, text="File name ", pady=5)
    fileNameL.grid(row=0, column=0, padx=10, pady=(50,0), columnspan=1)
    fileNameE = Entry(fileFrame)
    fileNameE.grid(row=0, column=1, padx=10, pady=(50,0), columnspan=1)

    btnFrame = Frame(topframe)
    btnFrame.pack()
    btnFrame.columnconfigure(0, weight=1)
    btnFrame.columnconfigure(1, weight=1)

    ok_btn = Button(btnFrame, text="OK", command=confirmName)
    ok_btn.grid(row=0, column=0, padx=5, pady=5, columnspan=1)
    cancel_btn = Button(btnFrame, text="Cancel", command=topframe.destroy)
    cancel_btn.grid(row=0, column=2, padx=5, pady=5, columnspan=1)


# edit functions
def copy():
    try:
        # copy to clipboard
        text.clipboard_clear()
        copyText = text.get(SEL_FIRST, SEL_LAST)
        text.clipboard_append(copyText)

        # update status
        # status_text2 = ' ' * 5 + "COPIED"
        # var.set(status_text1 + status_text2)

        return len(copyText)
    except TclError:
        print("[WARNING] Nothing selected")


def cut():
    copiedLength = copy()
    try:
        if copiedLength != 0:
            text.delete(SEL_FIRST, SEL_LAST)

            # update status
            # status_text2 = ' ' * 5 + "cut."
            # var.set(status_text1 + status_text2)

    except TclError:
        print("[WARNING] Nothing to cut")


def paste():
    copyText = text.clipboard_get()
    try:
        if len(copyText) != 0:
            text.insert(INSERT, copyText)

            # update status
            # status_text2 = ' ' * 5 + "pasted."
            # var.set(status_text1 + status_text2)
    except TclError:
        print("[WARNING] No data in clipboard")


# toolbar functions
def tool_new():
    newfile()


def tool_open():
    openfile()


def tool_save():
    save()


def tool_saveas():
    saveas()


def tool_copy():
    copy()


def tool_cut():
    cut()


def tool_paste():
    paste()


def change_fontfamily(event):
    f = Font(family=familyVar.get(), size=sizeVar.get())
    text.configure(font=f)


def change_fontsize(event):
    f = Font(family=familyVar.get(), size=sizeVar.get())
    text.configure(font=f)


# status bar functions
def countlines(event):
    global CURRENT_EDIT_STATUS
    CURRENT_EDIT_STATUS = 'UNSAVED'

    (line, c) = map(int, event.widget.index("end-1c").split("."))
    status_text1 = f"Status: INSERT MODE  ROW:{line}, COL:{c+1}    {CURRENT_EDIT_STATUS}"
    var.set(status_text1)


# pop-up menu functions
def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


# =================================
# main window
root = Tk()
root.title("Athensoft Text Editor - "+DEFAULT_FILE)
root.geometry("640x480+1250+5")
icon_img = ICON_LOGO
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

# --------------------------------
# popup menu
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Copy", command=copy)
popupmenu.add_command(label="Cut", command=cut)
popupmenu.add_separator()
popupmenu.add_command(label="Paste", command=paste)

# binding to root
root.bind("<Button-3>", showPopupMenu)

# --------------------------------
# toolbar
frame_toolbar = Frame(root, height=26)
frame_toolbar.pack(anchor=W)

btn0 = Button(frame_toolbar, text='New', command=tool_new, relief='groove')
btn0.pack(side=LEFT, padx=3)

btn1 = Button(frame_toolbar, text='Open', command=tool_open, relief='groove')
btn1.pack(side=LEFT, padx=3)

btn2 = Button(frame_toolbar, text='Save', command=tool_save, relief='groove')
btn2.pack(side=LEFT, padx=3)

btn3 = Button(frame_toolbar, text='Save as', command=tool_saveas, relief='groove')
btn3.pack(side=LEFT, padx=3)

btn4 = Button(frame_toolbar, text='Copy', command=tool_copy, relief='groove')
btn4.pack(side=LEFT, padx=3)

btn5 = Button(frame_toolbar, text='Cut', command=tool_cut, relief='groove')
btn5.pack(side=LEFT, padx=3)

btn6 = Button(frame_toolbar, text='Paste', command=tool_paste, relief='groove')
btn6.pack(side=LEFT, padx=3)

# arrow for option menu
arrow = PhotoImage(file=ICON_ARROW)

# font family
familyVar = StringVar()
familyList = ("Arial", "Times", "Courier", "微软雅黑")
familyVar.set(familyList[2])
family = OptionMenu(frame_toolbar, familyVar, *familyList, command=change_fontfamily)
family.pack(side=LEFT, pady=5, padx=(20, 5))
family.config(relief='groove', indicatoron=0, compound="right", image=arrow)

# font size
sizeVar = IntVar()
sizeList = [x for x in range(8, 25)]
sizeVar.set(sizeList[8])
size = OptionMenu(frame_toolbar, sizeVar, *sizeList, command=change_fontsize)
size.pack(side=LEFT, pady=5, padx=(0, 5))
size.config(relief='groove', indicatoron=0, compound="right", image=arrow)

# --------------------------------
# textarea
frame_text = Frame(root, height=30)
frame_text.pack(anchor=CENTER, fill=BOTH, expand=Y)

# text widget
text = Text(frame_text, height=5, width=30)
text.pack(side=LEFT, fill=BOTH, expand=Y)
fontDefault = Font(family="Courier", size=16)
text.configure(font=fontDefault)

# scrollbar
yscrollbar = Scrollbar(frame_text)
yscrollbar.pack(side=RIGHT, fill=Y)
yscrollbar.config(command=text.yview)
text.config(yscrollcommand=yscrollbar.set)

# listening
text.bind("<KeyRelease>", countlines)

# --------------------------------
# status bar
frame_status = Frame(root)
frame_status.pack(anchor=CENTER, fill=X)

# separator
sep = Separator(frame_status, orient=HORIZONTAL)
sep.pack(fill=X, padx=1)

# text on status bar
var = StringVar()

# for mode and position
status_text1 = "Status: INSERT MODE"

statusbar = Label(frame_status, textvariable=var)
statusbar.pack(side=BOTTOM, anchor=S + W)
var.set(status_text1)

# for status of saved or unsaved
status_text2 = ""

# --------------------------------

root.mainloop()
