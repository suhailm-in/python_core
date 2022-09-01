from tkinter import *
root=Tk()

label=Label(root,text="Hello World")       # label 1
label.pack()

Label(root,text="Hello New World").pack()  # label 2

root.mainloop()