"""
LabelFrame

"""

from tkinter import *

root = Tk()
root.title("Python GUI - LabelFrame")
root.geometry("320x160")
root.config(bg="#ddddff")

# data, dictionary
roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}

labfrm = LabelFrame(root, text = "Please choose your roles")

for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(labfrm, text = roles[i], variable = checkboxes[i]).pack()

labfrm.pack()

root.mainloop()
