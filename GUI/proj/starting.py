#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 09, 2018 03:52:32 AM PKT  platform: Windows NT

import sys

try:
    import Tkinter as tk
    from PIL import Image, ImageTk
except ImportError:
    import tkinter as tk
    from PIL import Image, ImageTk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import starting_support

def kill1(event):
    root.destroy()
    from p2 import vp_start_gui
    vp_start_gui()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    starting_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    starting_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Bernard MT Condensed} -size 28 -weight bold"  \
            " -slant roman -underline 0 -overstrike 0"

        top.geometry("600x272+464+331")
        top.title("Start")
        top.resizable(0, 0)
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.017, rely=0.037, relheight=0.93
                , relwidth=0.972)
        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(insertborderwidth="2")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=583)
        self.Canvas1.bind("<Button-1>", kill1)

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.24, rely=0.751, height=51, width=305)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        assert isinstance("COMMUNISTBADGER", str)
        self.Label1.configure(text='''COMMUNIST BADGER''')
        self.Label1.configure(width=305)

        self.original = Image.open('CommBadger.png')
        self.image = ImageTk.PhotoImage(self.original)
        self.Canvas2 = tk.Canvas(self.Canvas1)
        self.Canvas2.place(relx=0.274, rely=0.04, relheight=0.644
                , relwidth=0.468)
        self.Canvas2.configure(background="#ffffff")
        self.Canvas2.configure(highlightcolor="#ffffff")
        self.Canvas2.configure(highlightthickness="0")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief='ridge')
        self.Canvas2.configure(selectbackground="#ffffff")
        self.Canvas2.configure(selectforeground="black")
        self.Canvas2.configure(width=273)
        self.Canvas2.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")
        self.Canvas2.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.Canvas2.delete("IMG")
        self.Canvas2.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")

if __name__ == '__main__':
    vp_start_gui()





