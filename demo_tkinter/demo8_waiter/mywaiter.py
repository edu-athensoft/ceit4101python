"""

"""


import tkinter as tk
import tkinter.font as tkFont

from playsound import playsound

import threading
import time



def cmd1():
    def getup():
        playsound('snd/cmd1_getup.mp3')

    try:
        t = threading.Thread(target=getup, name='GetupThread')
        t.start()
    except:
        print
        "Error: unable to start thread"




def cmd2():
    def cook():
        playsound('snd/cmd2_cook.mp3')

    try:
        t = threading.Thread(target=cook, name='CookThread')
        t.start()
    except:
        print
        "Error: unable to start thread"


def cmd3():
    def drink():
        playsound('snd/cmd3_drink.mp3')

    try:
        t = threading.Thread(target=drink, name='DrinkThread')
        t.start()
    except:
        print
        "Error: unable to start thread"


def cmd4():
    def takeaway():
        playsound('snd/cmd4_takeaway.mp3')

    try:
        t = threading.Thread(target=takeaway, name='TakeawayThread')
        t.start()
    except:
        print
        "Error: unable to start thread"


def cmd5():
    def wish():
        playsound('snd/cmd5_wish.mp3')

    try:
        t = threading.Thread(target=wish, name='WishThread')
        t.start()
    except:
        print
        "Error: unable to start thread"

root = tk.Tk()

# settings
root.title("My Waiter v1.0")
root.geometry("640x480+300+200")

# font

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

mylabel = tk.Label(root, text='My Sweet Waiter', font=fontStyle)

# Get up!
mybtn1 = tk.Button(root, text='Wake-up', command=cmd1, padx=30,pady=20)

# Could you please cook some dishes for me?
mybtn2 = tk.Button(root, text='Cook', command=cmd2, padx=30,pady=20)

# Could you please bring me some tea?
mybtn3 = tk.Button(root, text='Drink', command=cmd3, padx=30,pady=20)

# Could you please take away these utensils?
mybtn4 = tk.Button(root, text='Clean', command=cmd4, padx=30,pady=20)


# Could you please take away these utensils?
mybtn5 = tk.Button(root, text='Wish', command=cmd5, padx=30,pady=20)


mylabel.grid(row=0)

mybtn1.grid(row=1,column=0)
mybtn2.grid(row=1,column=1)
mybtn3.grid(row=1,column=2)
mybtn4.grid(row=1,column=3)
mybtn5.grid(row=1,column=4)

tk.mainloop()