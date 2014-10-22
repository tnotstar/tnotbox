#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Borrowed from: http://www.dzone.com/snippets/xp-framepy-python3tkinter

"""
Program to do dynamic experimentation with the various padding and
border properties of a ttk.Frame. A frame is created and populated with
Three sub-frames:
 1. A set of spinboxes that adust the various padding parameters.
 2. A set of controls to adjust the border style and width
 3. A set of checkbuttons to alter the sticky values.
By changing different values you can arrive at a preferred appearance.
"""
#==============================================================================
# Create root window R and give its only row & column weight.
# The sticky property is ignored unless the containing widget has weight.
# Weight also makes it possible to stretch the window, but sticky would
# be ignored whether stretching was done or not.
#
from tkinter import *
from tkinter import ttk
R = Tk()
R.columnconfigure(0,weight=1)
R.rowconfigure(0,weight=1)

#==============================================================================
# create content frame C as R's only child.
# to make things clearer, give it a 5px solid border.

C = ttk.Frame(R, borderwidth=5, relief='solid' )

#==============================================================================
# Function called when any control changes: undisplay frame C and redisplay it
# with current configuration values. If the function is called as the
# command= parameter of e.g. a checkbox, there is no parameter. When called
# because it was bound to an event there is a parameter which can be ignored.

def somethingChanged(whatever=None):
    C.grid_remove()
    regridC()

#==============================================================================
# Function to display or redisplay frame C with current configuration options.
# Pedestrian coding style facilitates debugging.

def regridC():
    reliefstyle = value_R.get()
    C['relief'] = reliefstyle
    bw = sp_bw.get()
    C['borderwidth'] = bw
    C['padding'] = (sp_padL.get(),sp_padT.get(),sp_padR.get(),sp_padB.get())
    px = sp_padx.get()
    py = sp_pady.get()
    ix = sp_ipadx.get()
    iy = sp_ipady.get()
    st = makeSticky()
    C.grid( padx=px, pady=py, ipadx=ix, ipady=iy, sticky=st )


#=============================================================================
# Define a class for a small, labelled spinbox, of which we need several.
# Parameters are:
#     parent: widget within which the spinbox/frame will be gridded
#     text='   ': Text of label to precede the spinbox, s.b. short
#     minval=0: Minimum value of spinbox, and default starting value
#     maxval=99: Maximum value of spinbox
#     start=None: Starting value if other than minval
#     command=None: optional callback function, invoked when:
#        the up/down arrow of the spinbox is clicked
#        the up/down arrow key is pressed (at least on mac os)
#        keyboard focus leaves the box e.g. via a tab key or mouse click away
#        return key is pressed when focus is in the box
#        Note that the spinbox value need not have changed on these events.
# The returned object is a frame containing a label preceding a 2-digit
# numeric spinbox. Two methods are supplied:
#    object.grid() performs the grid operation on the frame, passing any
#         optional grid() parameters given.
#    object.get() returns the current value of the spinbox.
#    object.set() sets a new value of the spinbox.
#
class labelledSpinbox:
    """
    Define a small numeric spinbox with a label:
         labelledSpinbox(parent,text=,minval=,maxval=,start=,command=None)
         parent widget, label text, range of values, start, callback command
         methods: .grid(), .get(), .set()
    """
    def __init__(self, parent, text='   ', minval=0, maxval=99, start=None, command=None):
        self.frame = ttk.Frame(parent)
        self.label = ttk.Label(self.frame,text=text,width=len(text))
        self.spvar = StringVar()
        self.min, self.max = minval, maxval
        if start and (start<=self.max) and (start>=self.min):
            self.spvar.set(start)
        else:
            self.spvar.set(self.min)
        self.spox = Spinbox(self.frame,width=2,from_=self.min,to=self.max, \
                            textvariable=self.spvar,command=command)
        if command:
            self.spox.bind('<FocusOut>',func=command)
            self.spox.bind('<Key-Return>',func=command)
        self.label.grid(row=0,column=0)
        self.spox.grid (row=0,column=1)
    def grid(self, **kwargs): # grid with e.g. sticky, padx, whatever.
        return self.frame.grid(**kwargs)
    def get(self):
        return self.spvar.get()
    def set(self,n):
        if (n >= self.min) and (n <= self.max): # TypeError if n not numeric
            self.spvar.set(n)
            return n
        else:
            return None

#==============================================================================
# Make spinboxes for the Grid external padding parameters padx and pady
# and internal padding parameters ipadx and ipady. Group these in a
# frame labelled "grid opts"

GO = ttk.Frame(C, borderwidth=2,relief='groove', padding='2')
GOlb = ttk.Label(GO,text='grid opts'); GOlb.grid(row=0);
sp_padx = labelledSpinbox(GO, text='padx', command=somethingChanged)
sp_padx.grid(row=1)
sp_pady = labelledSpinbox(GO, text='pady', command=somethingChanged)
sp_pady.grid(row=2)
sp_ipadx = labelledSpinbox(GO, text='ipdx', command=somethingChanged)
sp_ipadx.grid(row=3)
sp_ipady = labelledSpinbox(GO, text='ipdy', command=somethingChanged)
sp_ipady.grid(row=4)
GO.grid(row=0,column=0)

#==============================================================================
# Make spinboxes for the Frame widget padding parameters L T R B (it is
# annoying that these are the 1-rotate of the CSS margin/padding values
# TRBL with its useful mnemonic of "trouble"). Group them in a frame
# labelled "frame opts".

FO = ttk.Frame(C, borderwidth=2,relief='groove', padding='2')
FOlb = ttk.Label(FO,text='frm opts'); FOlb.grid(row=0);
sp_padL = labelledSpinbox(FO, text='padL', command=somethingChanged)
sp_padL.grid(row=1)
sp_padT = labelledSpinbox(FO, text='padT', command=somethingChanged)
sp_padT.grid(row=2)
sp_padR = labelledSpinbox(FO, text='padR', command=somethingChanged)
sp_padR.grid(row=3)
sp_padB = labelledSpinbox(FO, text='padB', command=somethingChanged)
sp_padB.grid(row=4)
FO.grid(row=0,column=1)

#==============================================================================
# Make a set of radio buttons for the relief styles and a spinbox for the
# borderwidth. Enclose these in a frame headed "border".

BO = ttk.Frame(C, borderwidth=2,relief='groove', padding='2')
BOlb = ttk.Label(BO,text='border'); BOlb.grid(row=0);
sp_bw = labelledSpinbox(BO, text='bdw', start=5, command=somethingChanged)
sp_bw.grid(row=1)

value_R = StringVar()
value_R.set('solid')
rb_flat = ttk.Radiobutton(BO, text='Flat', value='flat',\
                          variable=value_R, command=somethingChanged)
rb_rais = ttk.Radiobutton(BO, text='Raised', value='raised',\
                          variable=value_R, command=somethingChanged)
rb_sunk = ttk.Radiobutton(BO, text='Sunken', value='sunken',\
                          variable=value_R, command=somethingChanged)
rb_soli = ttk.Radiobutton(BO, text='Solid', value='solid',\
                          variable=value_R, command=somethingChanged)
rb_ridg = ttk.Radiobutton(BO, text='Ridge', value='ridge',\
                          variable=value_R, command=somethingChanged)
rb_groo = ttk.Radiobutton(BO, text='Groove', value='groove',\
                          variable=value_R, command=somethingChanged)
rb_flat.grid(row=2,sticky=W)
rb_rais.grid(row=3,sticky=W)
rb_sunk.grid(row=4,sticky=W)
rb_soli.grid(row=5,sticky=W)
rb_ridg.grid(row=6,sticky=W)
rb_groo.grid(row=7,sticky=W)
BO.grid(row=0,column=2)

#==============================================================================
# Make a set of NSEW check-buttons and enclose them in a frame headed "sticky."
# Each has a value that is either the null string or its cardinal letter,
# initially null, hence the initial setting for C is sticky=''

value_N = StringVar(); value_N.set('')
value_S = StringVar(); value_S.set('')
value_E = StringVar(); value_E.set('')
value_W = StringVar(); value_W.set('')

# collect the current values of the buttons as a string
def makeSticky():
    return value_N.get()+value_S.get()+value_E.get()+value_W.get()

SO = ttk.Frame(C, borderwidth=2,relief='groove', padding='2')
SOlb = ttk.Label(SO,text='sticky')
SOlb.grid(row=0,columnspan=3,sticky=EW)

check_N = ttk.Checkbutton(SO, text='N', variable=value_N, onvalue='N',\
                          command=somethingChanged, offvalue='')
check_S = ttk.Checkbutton(SO, text='S', variable=value_S, onvalue='S',\
                          command=somethingChanged, offvalue='')
check_E = ttk.Checkbutton(SO, text='E', variable=value_E, onvalue='E',\
                          command=somethingChanged, offvalue='')
check_W = ttk.Checkbutton(SO, text='W', variable=value_W, onvalue='W',\
                          command=somethingChanged, offvalue='')

# Arrange the checkboxes in a cruciform layout --
# Ironically, it is not possible to achieve this layout using sticky!
# The use of sticky here keeps the checkboxes at the edge of the layout
# when it stretches. However, for that to work, both the rows and the
# columns of C have to be weighted.
SO.columnconfigure(0,weight=1); SO.rowconfigure(0,weight=1)
SO.columnconfigure(1,weight=1); SO.rowconfigure(1,weight=1)
SO.columnconfigure(2,weight=1); SO.rowconfigure(2,weight=1)
SO.rowconfigure(3,weight=1)
check_N.grid(row=1, column=1, sticky=N )
check_W.grid(row=2, column=0, sticky=W )
check_E.grid(row=2, column=2, sticky=E )
check_S.grid(row=3, column=1, sticky=S )
SO.grid(row=0,column=3)

#==============================================================================
# and away we go:

regridC()
R.mainloop()

# EOF