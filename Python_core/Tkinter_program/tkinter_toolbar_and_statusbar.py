from  tkinter import *
root=Tk()

toolbar=Frame(root,bg='yellow')
inbutton=Button(toolbar,text="crop")
inbutton.pack(side=LEFT,padx=2,pady=2)
iubutton=Button(toolbar,text='Exit',command=quit)
iubutton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)
statusbar=Label(root,text="this is status bar",fg="red",bg="gray",bd=2,anchor=W,relief='sunken')
statusbar.pack(side=BOTTOM,fill=X)



root.mainloop()