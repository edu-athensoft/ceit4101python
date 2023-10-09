#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5f
#  in conjunction with Tcl version 8.6
#    Oct 08, 2020 06:04:31 PM PDT  platform: Linux

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import demo.demo_tkinter.demo10_calendar.b_support as b_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    b_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    b_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'

        top.geometry("600x450+660+210")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0,  0)
        top.title("New Toplevel")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(x=250, y=80, height=37, width=94)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Button''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(x=280, y=180, height=75, width=125)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="wheat")
        self.Frame1.configure(highlightbackground="wheat")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(x=20, y=20, height=37, width=94)
        self.Button2.configure(activebackground="#f4bcb2")
        self.Button2.configure(background="wheat")
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(font="-family {DejaVu Sans Mono} -size 14")
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(text='''Button''')

if __name__ == '__main__':
    vp_start_gui()




