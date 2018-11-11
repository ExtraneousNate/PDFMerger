import tkinter as tk



counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
def WriteStuff():
    print(T.get(1.0, tk.END))


root =tk.Tk()

root.title=("Counting seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
frame =tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="Stop", width=15, command=root.destroy)
button.pack(side=tk.LEFT)
button2 = tk.Button(frame, text = "Print",width=15, command=WriteStuff)
button2.pack(side=tk.RIGHT)

T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "paste a list of files to be merged here")


whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text = whatever_you_do)
msg.pack()

root.mainloop()
