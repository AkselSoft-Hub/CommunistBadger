#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Green arrow Frame1
# Red arrow Frame 1_1

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

import searching_support

def kill1():
    root.destroy()
    from viewGraph import vp_start_gui2
    vp_start_gui2()
def kill2():
    root.destroy()
    from viewGraph2 import vp_start_gui2
    vp_start_gui2()
def back():
    root.destroy()
    from p2 import vp_start_gui
    vp_start_gui()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    searching_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    searching_support.init(w, top, *args, **kwargs)
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
        font11 = "-family {Shonar Bangla} -size 19 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 30 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Shonar Bangla} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family {Shonar Bangla} -size 20 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font21 = "-family {Shonar Bangla} -size 30 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font22 = "-family {Segoe UI} -size 19 -weight normal -slant "  \
            "roman -underline 1 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x454+440+187")
        top.title("Search")
        top.configure(background="#d9d9d9")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.017, rely=0.022, height=36, width=68)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font11)
        self.TLabel1.configure(relief='flat')
        self.TLabel1.configure(text='''Search:''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.133, rely=0.022, relheight=0.046
                , relwidth=0.777)
        self.TEntry1.configure(width=466)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.017, rely=0.088, relheight=0.888
                , relwidth=0.972)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#d9d9d9")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=583)

        self.Frame1 = tk.Frame(self.Canvas1)
        self.Frame1.place(relx=0.034, rely=0.05, relheight=0.186, relwidth=0.935)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=545)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.037, rely=0.133, height=48, width=65)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font15)
        self.Label1.configure(foreground="#1d73b5")
        self.Label1.configure(text='''FB''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.183, rely=0.133, height=40, width=15)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font14)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''''')
        self.Label2.configure(width=15)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.239, rely=0.133, height=23, width=87)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font17)
        self.Label3.configure(foreground="#1d73b5")
        self.Label3.configure(text='''''')
        self.Label3.configure(width=87)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.257, rely=0.4, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#56d86c")
        self.Button1.configure(disabledforeground="#000000")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#000000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(state='disabled')
        self.Button1.configure(text='''Hit''')
        self.Button1.configure(width=67)

        self.original = Image.open('green-arrow.png')
        self.image = ImageTk.PhotoImage(self.original)
        self.Canvas2 = tk.Canvas(self.Frame1)
        self.Canvas2.place(relx=0.661, rely=0.267, relheight=0.573
                , relwidth=0.079)
        self.Canvas2.configure(background="#d9d9d9")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="#d9d9d9")
        self.Canvas2.configure(relief='ridge')
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")
        self.Canvas2.configure(width=43)
        self.Canvas2.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")
        self.Canvas2.bind("<Configure>", self.resize)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.44, rely=0.133, relheight=0.733, relwidth=0.174)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=95)

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.105, rely=0.182, height=36, width=15)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font21)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''''')
        self.Label4.configure(width=1)

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.316, rely=0.182, height=31, width=56)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font22)
        self.Label5.configure(foreground="#1d73b5")
        self.Label5.configure(text='''0.018''')
        self.Label5.configure(width=60)

        self.Button2 = tk.Button(self.Frame1, command = kill2)
        self.Button2.place(relx=0.807, rely=0.267, height=34, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''View Graph''')
        self.Button2.configure(width=87)

        self.Frame1_1 = tk.Frame(self.Canvas1)
        self.Frame1_1.place(relx=0.034, rely=0.298, relheight=0.186
                , relwidth=0.935)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(background="#d9d9d9")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")
        self.Frame1_1.configure(width=545)

        self.Label1_2 = tk.Label(self.Frame1_1)
        self.Label1_2.place(relx=0.037, rely=0.133, height=48, width=65)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font15)
        self.Label1_2.configure(foreground="#1d73b5")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        stockName = "EBAY"
        assert isinstance(stockName, str)
        self.Label1_2.configure(text=stockName)

        self.Label2_3 = tk.Label(self.Frame1_1)
        self.Label2_3.place(relx=0.183, rely=0.133, height=40, width=15)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font14)
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''''')

        self.Label3_4 = tk.Label(self.Frame1_1)
        self.Label3_4.place(relx=0.239, rely=0.133, height=23, width=87)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font=font17)
        self.Label3_4.configure(foreground="#1d73b5")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        compName = ""
        assert isinstance(compName, str)
        self.Label3_4.configure(text=compName)

        self.Button1_5 = tk.Button(self.Frame1_1)
        self.Button1_5.place(relx=0.257, rely=0.4, height=24, width=67)
        self.Button1_5.configure(activebackground="#ececec")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#d81a46")
        self.Button1_5.configure(disabledforeground="#000000")
        self.Button1_5.configure(foreground="#000000")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(state='disabled')
        self.Button1_5.configure(text='''Miss''')

        self.original1 = Image.open('red-arrow.png')
        self.image1 = ImageTk.PhotoImage(self.original1)
        self.Canvas2_6 = tk.Canvas(self.Frame1_1)
        self.Canvas2_6.place(relx=0.661, rely=0.267, relheight=0.573
                , relwidth=0.079)
        self.Canvas2_6.configure(background="#d9d9d9")
        self.Canvas2_6.configure(highlightbackground="#d9d9d9")
        self.Canvas2_6.configure(highlightcolor="#d9d9d9")
        self.Canvas2_6.configure(insertbackground="#000000")
        self.Canvas2_6.configure(relief='ridge')
        self.Canvas2_6.configure(selectbackground="#c4c4c4")
        self.Canvas2_6.configure(selectforeground="black")
        self.Canvas2_6.configure(width=43)
        self.Canvas2_6.create_image(0, 0, image=self.image1, anchor='nw', tags="IMG")
        self.Canvas2_6.bind("<Configure>", self.resize2)

        self.Frame2_7 = tk.Frame(self.Frame1_1)
        self.Frame2_7.place(relx=0.44, rely=0.133, relheight=0.733
                , relwidth=0.174)
        self.Frame2_7.configure(relief='groove')
        self.Frame2_7.configure(borderwidth="2")
        self.Frame2_7.configure(relief='groove')
        self.Frame2_7.configure(background="#d9d9d9")
        self.Frame2_7.configure(highlightbackground="#d9d9d9")
        self.Frame2_7.configure(highlightcolor="black")
        self.Frame2_7.configure(width=95)

        self.Label4_8 = tk.Label(self.Frame2_7)
        self.Label4_8.place(relx=0.105, rely=0.182, height=36, width=15)
        self.Label4_8.configure(activebackground="#f9f9f9")
        self.Label4_8.configure(activeforeground="black")
        self.Label4_8.configure(background="#d9d9d9")
        self.Label4_8.configure(disabledforeground="#a3a3a3")
        self.Label4_8.configure(font=font21)
        self.Label4_8.configure(foreground="#000000")
        self.Label4_8.configure(highlightbackground="#d9d9d9")
        self.Label4_8.configure(highlightcolor="black")
        self.Label4_8.configure(text='''''')

        self.Label5_9 = tk.Label(self.Frame2_7)
        self.Label5_9.place(relx=0.316, rely=0.182, height=31, width=56)
        self.Label5_9.configure(activebackground="#f9f9f9")
        self.Label5_9.configure(activeforeground="black")
        self.Label5_9.configure(background="#d9d9d9")
        self.Label5_9.configure(disabledforeground="#a3a3a3")
        self.Label5_9.configure(font=font22)
        self.Label5_9.configure(foreground="#1d73b5")
        self.Label5_9.configure(highlightbackground="#d9d9d9")
        self.Label5_9.configure(highlightcolor="black")
        price = "0.04"
        assert isinstance(price, str)
        self.Label5_9.configure(text=price)

        self.Button2_10 = tk.Button(self.Frame1_1, command = kill1)
        self.Button2_10.place(relx=0.807, rely=0.267, height=34, width=87)
        self.Button2_10.configure(activebackground="#ececec")
        self.Button2_10.configure(activeforeground="#000000")
        self.Button2_10.configure(background="#d9d9d9")
        self.Button2_10.configure(disabledforeground="#a3a3a3")
        self.Button2_10.configure(foreground="#000000")
        self.Button2_10.configure(highlightbackground="#d9d9d9")
        self.Button2_10.configure(highlightcolor="black")
        self.Button2_10.configure(pady="0")
        self.Button2_10.configure(text='''View Graph''')

        self.Button3 = tk.Button(top, command= back)
        self.Button3.place(relx=0.917, rely=0.022, height=24, width=37)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Back''')
        self.Button3.configure(width=37)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size, Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.Canvas2.delete("IMG")
        self.Canvas2.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")

    def resize2(self, event):
        size = (event.width, event.height)
        resized = self.original1.resize(size, Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(resized)
        self.Canvas2_6.delete("IMG")
        self.Canvas2_6.create_image(0, 0, image=self.image1, anchor='nw', tags="IMG")





