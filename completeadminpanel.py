#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Feb 24, 2019 04:33:38 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import adminpanel_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Admin_Panel_ (root)
    adminpanel_support.init(root, top)
    root.mainloop()

w = None
def create_Admin_Panel_(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Admin_Panel_ (w)
    adminpanel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Admin_Panel_():
    global w
    w.destroy()
    w = None


class Admin_Panel_:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Minion Pro SmBd} -size 9 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1320x855+242+93")
        top.title("Admin Panel ")
        top.configure(background="#2fd823")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.08, rely=0.02, height=23, width=78)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#2fd823")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Add Goods''')

        self.goodname = Label(top)
        self.goodname.place(relx=0.02, rely=0.12, height=27, width=91)
        self.goodname.configure(activebackground="#ddef64")
        self.goodname.configure(activeforeground="#000000")
        self.goodname.configure(background="#ced877")
        self.goodname.configure(disabledforeground="#a3a3a3")
        self.goodname.configure(font=font9)
        self.goodname.configure(foreground="#000000")
        self.goodname.configure(highlightbackground="#efa82d")
        self.goodname.configure(highlightcolor="black")
        self.goodname.configure(text='''Good Name :''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.09, rely=0.12, relheight=0.03, relwidth=0.13)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.goodcount = Label(top)
        self.goodcount.place(relx=0.02, rely=0.16, height=27, width=93)
        self.goodcount.configure(activebackground="#ef733e")
        self.goodcount.configure(activeforeground="black")
        self.goodcount.configure(background="#ced877")
        self.goodcount.configure(disabledforeground="#a3a3a3")
        self.goodcount.configure(font=font9)
        self.goodcount.configure(foreground="#000000")
        self.goodcount.configure(highlightbackground="#d9d9d9")
        self.goodcount.configure(highlightcolor="black")
        self.goodcount.configure(text='''Good Count :''')

        self.TEntry2 = ttk.Entry(top)
        self.TEntry2.place(relx=0.09, rely=0.16, relheight=0.03, relwidth=0.13)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.02, rely=0.21, height=27, width=85)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ced877")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Good Price :''')

        self.TEntry3 = ttk.Entry(top)
        self.TEntry3.place(relx=0.09, rely=0.21, relheight=0.03, relwidth=0.13)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="ibeam")

        self.Label5 = Label(top)
        self.Label5.place(relx=0.03, rely=0.07, height=27, width=70)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ced877")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Good ID :''')

        self.TEntry4 = ttk.Entry(top)
        self.TEntry4.place(relx=0.09, rely=0.07, relheight=0.03, relwidth=0.13)
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="ibeam")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.04, rely=0.26, height=87, width=218)
        self.TButton1.configure(command=adminpanel_support.addtodb)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Add to Database''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Label2 = Label(top)
        self.Label2.place(relx=0.33, rely=0.02, height=23, width=95)
        self.Label2.configure(background="#2fd823")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Delete Goods''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.29, rely=0.07, height=27, width=60)
        self.Label3.configure(background="#d86b34")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Good ID''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.27, rely=0.12, height=27, width=83)
        self.Label6.configure(background="#d86b34")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Good Count''')

        self.TEntry5 = ttk.Entry(top)
        self.TEntry5.place(relx=0.36, rely=0.07, relheight=0.03, relwidth=0.06)
        self.TEntry5.configure(width=76)
        self.TEntry5.configure(takefocus="")
        self.TEntry5.configure(cursor="ibeam")

        self.TEntry6 = ttk.Entry(top)
        self.TEntry6.place(relx=0.36, rely=0.12, relheight=0.03, relwidth=0.06)
        self.TEntry6.configure(width=76)
        self.TEntry6.configure(takefocus="")
        self.TEntry6.configure(cursor="ibeam")

        self.deletegoods = ttk.Button(top)
        self.deletegoods.place(relx=0.3, rely=0.18, height=67, width=168)
        self.deletegoods.configure(takefocus="")
        self.deletegoods.configure(text='''Delete''')
        self.deletegoods.configure(width=168)

        self.Label7 = Label(top)
        self.Label7.place(relx=0.58, rely=0.02, height=23, width=100)
        self.Label7.configure(background="#2fd823")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Add Employee''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.52, rely=0.07, height=23, width=45)
        self.Label8.configure(background="#d875a0")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font9)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''eid''')
        self.Label8.configure(width=45)

        self.Label9 = Label(top)
        self.Label9.place(relx=0.5, rely=0.12, height=27, width=75)
        self.Label9.configure(background="#d875a0")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font9)
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''First Name''')

        self.Label10 = Label(top)
        self.Label10.place(relx=0.5, rely=0.16, height=27, width=72)
        self.Label10.configure(background="#d875a0")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font9)
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Last Name''')

        self.Label11 = Label(top)
        self.Label11.place(relx=0.48, rely=0.21, height=27, width=104)
        self.Label11.configure(background="#d875a0")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font=font9)
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Mobile Number''')

        self.TEntry7 = ttk.Entry(top)
        self.TEntry7.place(relx=0.58, rely=0.07, relheight=0.03, relwidth=0.13)
        self.TEntry7.configure(takefocus="")
        self.TEntry7.configure(cursor="ibeam")

        self.TEntry8 = ttk.Entry(top)
        self.TEntry8.place(relx=0.58, rely=0.12, relheight=0.03, relwidth=0.13)
        self.TEntry8.configure(takefocus="")
        self.TEntry8.configure(cursor="ibeam")

        self.TEntry9 = ttk.Entry(top)
        self.TEntry9.place(relx=0.58, rely=0.16, relheight=0.03, relwidth=0.13)
        self.TEntry9.configure(takefocus="")
        self.TEntry9.configure(cursor="ibeam")

        self.TEntry10 = ttk.Entry(top)
        self.TEntry10.place(relx=0.58, rely=0.21, relheight=0.03, relwidth=0.13)
        self.TEntry10.configure(takefocus="")
        self.TEntry10.configure(cursor="ibeam")

        self.addemployee = ttk.Button(top)
        self.addemployee.place(relx=0.54, rely=0.27, height=77, width=188)
        self.addemployee.configure(takefocus="")
        self.addemployee.configure(text='''Add Employee''')
        self.addemployee.configure(width=188)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.79, rely=0.02, height=21, width=115)
        self.TLabel1.configure(background="#2fd823")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Delete Employee''')

        self.Label12 = Label(top)
        self.Label12.place(relx=0.76, rely=0.07, height=23, width=61)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font=font9)
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''eid''')
        self.Label12.configure(width=61)

        self.TEntry11 = ttk.Entry(top)
        self.TEntry11.place(relx=0.82, rely=0.07, relheight=0.03, relwidth=0.07)
        self.TEntry11.configure(width=96)
        self.TEntry11.configure(takefocus="")
        self.TEntry11.configure(cursor="ibeam")

        self.deleteemployee = ttk.Button(top)
        self.deleteemployee.place(relx=0.77, rely=0.12, height=57, width=171)
        self.deleteemployee.configure(takefocus="")
        self.deleteemployee.configure(text='''Delete Employee''')
        self.deleteemployee.configure(width=171)

        self.Label13 = Label(top)
        self.Label13.place(relx=0.09, rely=0.43, height=23, width=100)
        self.Label13.configure(background="#2fd823")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Add Customer''')

        self.Label14 = Label(top)
        self.Label14.place(relx=0.04, rely=0.5, height=23, width=91)
        self.Label14.configure(background="#0dd8bd")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font=font9)
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''First Name''')
        self.Label14.configure(width=91)

        self.Label15 = Label(top)
        self.Label15.place(relx=0.04, rely=0.56, height=23, width=91)
        self.Label15.configure(background="#0dd8bd")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font=font9)
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Last Name''')
        self.Label15.configure(width=91)

        self.Label16 = Label(top)
        self.Label16.place(relx=0.04, rely=0.62, height=27, width=49)
        self.Label16.configure(background="#0dd8bd")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font=font9)
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Mobile''')

        self.Label17 = Label(top)
        self.Label17.place(relx=0.04, rely=0.68, height=27, width=57)
        self.Label17.configure(background="#0dd8bd")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font=font9)
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Address''')

        self.TEntry12 = ttk.Entry(top)
        self.TEntry12.place(relx=0.12, rely=0.5, relheight=0.03, relwidth=0.13)
        self.TEntry12.configure(takefocus="")
        self.TEntry12.configure(cursor="ibeam")

        self.TEntry13 = ttk.Entry(top)
        self.TEntry13.place(relx=0.12, rely=0.56, relheight=0.03, relwidth=0.13)
        self.TEntry13.configure(takefocus="")
        self.TEntry13.configure(cursor="ibeam")

        self.TEntry14 = ttk.Entry(top)
        self.TEntry14.place(relx=0.12, rely=0.62, relheight=0.03, relwidth=0.13)
        self.TEntry14.configure(takefocus="")
        self.TEntry14.configure(cursor="ibeam")

        self.TEntry15 = ttk.Entry(top)
        self.TEntry15.place(relx=0.12, rely=0.68, relheight=0.03, relwidth=0.13)
        self.TEntry15.configure(takefocus="")
        self.TEntry15.configure(cursor="ibeam")

        self.addcustomer = ttk.Button(top)
        self.addcustomer.place(relx=0.06, rely=0.74, height=57, width=168)
        self.addcustomer.configure(takefocus="")
        self.addcustomer.configure(text='''Add Customer''')
        self.addcustomer.configure(width=168)

        self.Label18 = Label(top)
        self.Label18.place(relx=0.42, rely=0.43, height=23, width=117)
        self.Label18.configure(background="#2fd823")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''Delete Customer''')

        self.Label19 = Label(top)
        self.Label19.place(relx=0.34, rely=0.5, height=23, width=78)
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(text='''First Name''')

        self.Label20 = Label(top)
        self.Label20.place(relx=0.34, rely=0.56, height=23, width=77)
        self.Label20.configure(background="#d9d9d9")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Last Name''')

        self.TEntry16 = ttk.Entry(top)
        self.TEntry16.place(relx=0.42, rely=0.5, relheight=0.03, relwidth=0.13)
        self.TEntry16.configure(takefocus="")
        self.TEntry16.configure(cursor="ibeam")

        self.TEntry17 = ttk.Entry(top)
        self.TEntry17.place(relx=0.42, rely=0.56, relheight=0.03, relwidth=0.13)
        self.TEntry17.configure(takefocus="")
        self.TEntry17.configure(cursor="ibeam")

        self.deletecustomer = ttk.Button(top)
        self.deletecustomer.place(relx=0.37, rely=0.63, height=67, width=181)
        self.deletecustomer.configure(takefocus="")
        self.deletecustomer.configure(text='''Delete Customer''')
        self.deletecustomer.configure(width=181)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="Arial 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event, *args, **kwargs):
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="Arial 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()


