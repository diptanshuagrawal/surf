from Tkinter import *
import ttk
import os
import numpy as np
import cv2
import sqlite3
import datacreatenew
import recognizer


def btnCallback():
    #extract the textbox variable
    x = entry_1.get()
    y = entry_2.get()
    z = entry_3.get()
    w = entry_4.get()
    v = entry_5.get()
    datacreatenew.create(y,"\""+x+"\"",z,"\""+w+"\"","\""+v+"\"")
    import trainer

def rfidcall():
        r = entry_6.get()
        recognizer.rec(int(r))

        
    
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label_1 = Label(topFrame, text="Name")
label_2 = Label(topFrame, text="ID")
label_3 = Label(topFrame, text="Age")
label_4 = Label(topFrame, text="Gender")
label_5 = Label(topFrame, text="CriminalRecord")
entry_1 = Entry(topFrame)
entry_2 = Entry(topFrame)
entry_3 = Entry(topFrame)
entry_4 = Entry(topFrame)
entry_5 = Entry(topFrame)

# widgets centered by default, sticky option to change
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)
label_4.grid(row=3, sticky=E)
label_5.grid(row=4, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)
entry_5.grid(row=4, column=1)

label_7 = Button(topFrame, text="Submit", command=btnCallback)
label_7.grid(row=5, column=1)

labelframe = LabelFrame(root, text="Run software")
labelframe.pack(fill="both", expand="yes")
 
label_6 = Label(labelframe, text="RFID")
entry_6 = Entry(labelframe)
label_6.grid(row=6, sticky=E)
entry_6.grid(row=6, column=1)
label_7 = Button(labelframe, text="START!", command = rfidcall )
label_7.grid(row=7,column=1)



# widgets can take up more than one cell with columnspan and rowspan
#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)

root.mainloop()



