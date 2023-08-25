"""
Tkinter

a label counter

config()
after()
"""


from tkinter import *


def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    counting()


root = Tk()

root.title('Python GUI - Label counter')

root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

#
counter = 0

# label object
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 10,
              font = "Helvetic 30 bold")
digit_label.pack()

# counting
run_counter(digit_label)


root.mainloop()