from tkinter import *
root=Tk()

lable1=Label(root,text="Hello Welcome",bg="red")
lable1.pack(fill=X)
lable2=Label(root,text="Hello World",bg="yellow")
lable2.pack(side=LEFT,fill=Y)
lable3=Label(root,text="Hello vector",bg="green")
lable3.pack(side=RIGHT,fill=Y)
lable1=Label(root,text="Hello End",bg="blue")
lable1.pack(fill=X)

root.mainloop()