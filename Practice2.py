import tkinter as tk
from tkinter import filedialog


def WriteStuff():
    print(T.get(1.0, tk.END))

def BrowseFolder():
    filename=filedialog.askdirectory()
    global folderPath
    folderPath.set(filename)

root =tk.Tk()

folderPath = tk.StringVar()
label = tk.Label(root, textvariable=folderPath)
label.pack()
frame =tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="Close", width=15, command=root.destroy)
button.pack(side=tk.LEFT)
button2 = tk.Button(frame, text = "Print",width=15, command=WriteStuff)
button2.pack(side=tk.RIGHT)
button3 = tk.Button(frame, text="Browse", width =15, command=BrowseFolder)
button3.pack(side=tk.RIGHT)

T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "paste a list of files to be merged here")


whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text = whatever_you_do)
msg.pack()

root.mainloop()
