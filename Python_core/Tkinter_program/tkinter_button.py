from tkinter import *
root=Tk()

#lable
lable=Label(root,text="Hello World")
lable.pack()

#button 1
but=Button(root,text="login",fg="red",bg="yellow")
but.pack()

#button in frame
framme1=Frame(root)
framme1.pack()
Button(framme1,text="logout",fg="blue",bg="gray").pack()


root.mainloop()