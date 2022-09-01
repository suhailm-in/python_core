from  tkinter import *
root=Tk()

Label(root,text="Enter your name").pack()

entry=Entry(root)
entry.pack()

Label(root,text="Enter Password").pack()
Entry(root,fg="red").pack()
root.mainloop()