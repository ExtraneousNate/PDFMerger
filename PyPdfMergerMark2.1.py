from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter
import pandas as pd
import csv



#i think this is the name of the main window

top = tkinter.Tk()
#the size of the window
top.geometry("400x400")

#a test function definition
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

#a function to let the user browse for a bom & write the file path somewhere and maybe process the data
def BomList():
    top.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),))
    FilePath=(top.filename)



    #open and read the csv files

    with open(FilePath, "rt", newline="", encoding="ascii") as csvfile:
        datareader = csv.reader(csvfile)
        Data =[]
        #add column 2 of each row to a list with white space removed
        for row in datareader:
            Data.append(row[2].strip())


    #remove list items that are blank
    Data=list(filter(None, Data))
    LabelString=""
    for item in Data:
        LabelString=LabelString+(item+"*.pdf "+item+"*.dxf ")
    print(LabelString)
    #show to data on the GUI
    w = Label(top, text=LabelString)
    w.pack()
    T = Text(top, height=5, width=16)
    T.pack()
    T.insert(END,LabelString)

def SearchList():
    top.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),))
    FilePath=(top.filename)



    #open and read the csv files

    with open(FilePath, "rt", newline="", encoding="ascii") as csvfile:
        datareader = csv.reader(csvfile)
        Data =[]
        #add column 2 of each row to a list with white space removed
        for row in datareader:
            Data.append(row[1].strip())


    #remove list items that are blank
    Data=list(filter(None, Data))


BomBrowse = Button(top, text = "Browse", command = BomList)
SearchBrowse = Button(top, text = "Browse", command = SearchList)
BomBrowse.place(x = 50,y = 100)
SearchBrowse.place(x=150,y=100)
# T = Text(top, height=2, width=30)
# T.pack()
# T.insert(END, BomList)
top.mainloop()
