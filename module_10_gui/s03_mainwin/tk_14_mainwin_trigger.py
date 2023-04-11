"""

"""

from tkinter import *
import time
import datetime

def showTime():
    # text.insert(END, str(time.time())+'\n')
    # insert text at the END

    # text.insert(END, datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")+'\n')

    # please compare this with the one above
    text.insert(END, datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))

    # set focus at the last line
    text.see(END)
    text.insert(END, '\n')

    # ms: million second
    ms = 1000
    root.after(ms, showTime)  # again forever

root = Tk()
root.title("Python GUI - Timer")

icon_img = 'athens-logo.ico'
root.iconbitmap(icon_img)

root.geometry("640x480+400+300")
root.configure(bg="#ddddff")

#
text = Text(root, height = 5)
text.pack(side=BOTTOM)

root.after(1000, showTime)



root.mainloop()
