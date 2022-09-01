from tkinter import *
root=Tk()
la1=Label(root,text="Username :")
la2=Label(root,text="Mobile :")
la3=Label(root,text="Age :")
la4=Label(root,text="New Password :")
la5=Label(root,text="Re Password :")

en1=Entry(root)
en2=Entry(root)
en3=Entry(root)
en4=Entry(root)
en5=Entry(root)

but1=Button(root,text="login")
but2=Button(root,text="clear")

la1.grid(row=0,column=0)
en1.grid(row=0,column=1)
la2.grid(row=1,column=0)
en2.grid(row=1,column=1)
la3.grid(row=2,column=0)
en3.grid(row=2,column=1)
la4.grid(row=3,column=0)
en4.grid(row=3,column=1)
la5.grid(row=4,column=0)
en5.grid(row=4,column=1)
but1.grid(row=5,column=0)
but2.grid(row=5,column=1)


root.mainloop()