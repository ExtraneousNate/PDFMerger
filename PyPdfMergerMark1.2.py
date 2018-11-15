from PyPDF2 import PdfFileMerger
from tkinter import *

global Path

global FileNames

def MergFile():
    merger = PdfFileMerger()
    #
    # Path = input("Please enter the file path that contains the pdf files")
    # FileString = input("Please past in the space seperated file list from excel")
    # #Path = "C:\\Users\\HUFFMANN\\Desktop\\temp--\\test bom merging"
    # #FileString = "2038308.pdf 2038302.pdf 2038303.pdf 2038330.pdf 2038249.pdf 2038313.pdf 2038334.pdf 2038273.pdf 2002612.pdf 2027433.pdf 2038318.pdf 2038256.pdf 2038270.pdf 2038337.pdf 2038338.pdf 2038272.pdf 2038352.pdf 2038354.pdf 2038740.pdf"
    FileList = FileNames.split()
    #
    for file in FileList:
        merger.append(fileobj = Path+"\\" +file)
    #
    merger.write(Path+"\\PrintPackage.pdf")

root = Tk()
root.geometry("500x400")
root.title('Paste String Here')

Path = Entry(root)
Path.pack()
Path.place(rely=.33)
Path.focus_set()

FileNames = Entry(root)
FileNames.place(rely=.66)
FileNames = Pack()


b = Button(root,text='okay',command=MergFile)
b.pack(side='bottom')

root.mainloop()
