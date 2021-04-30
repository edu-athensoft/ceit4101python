"""

"""

from tkinter import *
import time
import datetime

def showTime():
    # text.insert(END, str(time.time())+'\n')
    # insert text at the END
    print(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))

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
root.after(1000, showTime)

root.mainloop()
