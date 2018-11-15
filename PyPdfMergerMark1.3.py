from PyPDF2 import PdfFileMerger

import tkinter as tk
# library for browsing to file loctions
from tkinter import filedialog

# this will be where the pdf merging code goes
def MergePDF():
    print(T.get(1.0, tk.END))


    merger = PdfFileMerger()

    Path = folderPath.get()
    FileString = T.get(1.0, tk.END)
    #Path = "C:\\Users\\HUFFMANN\\Desktop\\temp--\\test bom merging"
    #FileString = "2038308.pdf 2038302.pdf 2038303.pdf 2038330.pdf 2038249.pdf 2038313.pdf 2038334.pdf 2038273.pdf 2002612.pdf 2027433.pdf 2038318.pdf 2038256.pdf 2038270.pdf 2038337.pdf 2038338.pdf 2038272.pdf 2038352.pdf 2038354.pdf 2038740.pdf"
    FileList = FileString.split(",")

    for file in FileList:
        file=file.strip()
        print(file)
        merger.append(fileobj = Path+"\\" +file)

    merger.write(Path+"\\PrintPackage.pdf")

# function for browsing to the pdf file locaitons
def BrowseFolder():
    # prompt user
    filename=filedialog.askdirectory()
    # declare global variable to make the data available
    global folderPath
    # put the file path in the global varriable
    folderPath.set(filename)

# declaire the main window
root =tk.Tk()

# This apparently needs to be here so that label2 can access the data
folderPath = tk.StringVar()

# An instruction lable
label1 = tk.Label(root, text = "Browse to the location of the .pdf files")
# putting it at the top left
label1.grid(row=0)
# a lable to show the user what path they browed to
label2 = tk.Label(root, textvariable=folderPath)
# positioning the lable
label2.grid(row=1)


# a button to close the program
button = tk.Button(root, text="Close", width=15, command=root.destroy)
# positioning the close button
button.grid(row=5, column = 1)
# this will become the merge button
button2 = tk.Button(root, text = "Merge",width=15, command=MergePDF)
# positioning the merge button
button2.grid(row=4, column=1)
# a button to browse for the folder location
button3 = tk.Button(root, text="Browse", width =15, command=BrowseFolder)
# positioning the browse button
button3.grid(row=1, column = 1)


# a textbox where the user can past a list of the files
T = tk.Text(root, height=4, width=60)
# positioning the text box
T.grid(row = 4 )
# putting instruction in the text box
T.insert(tk.END, "Paste a list of files here in the order you want them to be merged. File names must be comma seperated and include the "".pdf"" extention")
# select the instructions so they can easily be overwrited with a paste command
T.tag_add(tk.SEL, "1.0", tk.END)
# setting the cursor in the textbox
T.focus_set()



root.mainloop()



# b = Button(root,text='okay',command=MergFile)
# b.pack(side='bottom')
#
# root.mainloop()
