from PyPDF2 import PdfFileMerger

import tkinter as tk
# library for browsing to file loctions
from tkinter import filedialog

# this will be where the pdf merging code goes
def MergePDF():
    # print(T.get(1.0, tk.END))

    # creating the object to be merged into
    merger = PdfFileMerger()

    # Get the file path the user has browsed for
    Path = folderPath.get()

    # Get a string for the list of files to be merged
    FileString = T.get(1.0, tk.END)

    # split the string by commas
    FileList = FileString.split(",")

    # Get the size of the list of files to be merged
    ListCount=len(FileList)

    # for testing and trouble shooting purposes
    print(ListCount)

    # loop through eash object in the string
    for file in FileList:
        # Remove any extra white space from the file names
        file=file.strip()
        # print file name for testing and trouble shooting
        print(file)
        # error handling
        try:
            # Merging the file onto the existing merge object
            merger.append(fileobj = Path+"\\" +file)
        # Main error is FileNotFoundError
        except FileNotFoundError:
            # Create a new window to display the error
            win = tk.Toplevel()
            win.wm_title("Window")
            # Label in error window
            l1 = tk.Label(win, text="The following files was not found:")
            l1.grid(row=0)
            # label to display the name of the file that caused the error
            l2 = tk.Label(win, text=file)
            l2.grid(row=1, column=0)

            l3 = tk.Label(win, text="Merge Failed")
            l3.grid(row=2)
            # Button to close the error message window
            b = tk.Button(win, text="Close", width = 15, command=win.destroy)
            b.grid(row=3, column=0)

            b2 = tk.Button(win,text = "Browse", width = 15, command=BrowseMissingFile)
            b2.grid(row=3, column=1)

            # I think this will kick the program out of the merge routine on error
            return 0

    # write the merged data to a file when merging is complete
    # Could add some error hanging here for where it can't overwrited the existing file because it is currently open
    merger.write(Path+"\\PrintPackage.pdf")

# function for browsing to the pdf file locaitons
def BrowseFolder():
    # prompt user
    filename=filedialog.askdirectory()
    # declare global variable to make the data available
    global folderPath
    # put the file path in the global varriable
    folderPath.set(filename)

#fucntion to allow the user to select a file to merge in a browse window
def BrowseMissingFile():
    #prompt user to select file
    filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("pdf files","*.pdf")])
    #declare a global variable to store the file selected
    global missingPdf
    
    missingPdf=filename

# SOME REF CODE THAT CAN BE USED TO MAKE A PROGRESS WINDOW
# def OpenProgressWindow():
#     win = tk.Toplevel()
#     win.wm_title("Window")
#
#     l = tk.Label(win, text="Input")
#     l.grid(row=0, column=0)
#
#     b = tk.Button(win, text="Okay", command=win.destroy)
#     b.grid(row=1, column=0)

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
